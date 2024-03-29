import scipy.stats as ss
import itertools as it
import pandas as pd
import numpy as np

from bisect import bisect_left
from typing import List
from pandas import Categorical

import ast

def apfd(nqueries: list, hypsize: list, max_nqueries=None):
    hs = hypsize
    nq = nqueries
    assert hs[0] == 1
    assert len(nq) == len(hs)
    
    extra_nqueries, extra_hs = [],[]
    if(not max_nqueries is None): 
        extra_nqueries = [max_nqueries]
        extra_hs = [hs[-1]]

    return 1 - (np.sum(np.multiply([*nq,*extra_nqueries], np.diff([0, *hs,*extra_hs]))) / (np.max([*nq,*extra_nqueries]) * np.max(hs))) + (1.0 / (2 * np.max([*nq,*extra_nqueries])))

def auc_learning(nqueries: list, hypsize: list, max_nqueries=None):
    hs = hypsize
    nq = nqueries
    assert hs[0] == 1
    assert len(nq) == len(hs)
    
    extra_nqueries, extra_hs = [],[]
    if(not max_nqueries is None): 
        extra_nqueries = [max_nqueries]
        extra_hs = [hs[-1]]
    
    return np.trapz([*hs,*extra_hs],[*nq,*extra_nqueries])

def derive_data(data_frame: pd.DataFrame.dtypes):
    # first, copy dataframe
    df = data_frame.copy()
    
    # rename soucha CTTs and set CTTs as Categorical data 
    df['CTT'] = df['CTT'].str.replace('Soucha','')
    df['CTT'] = df['CTT'].str.replace('HadsInt', 'H-ADS')
    df['CTT'] = df['CTT'].str.replace('SPYH', 'SPY-H')
    df['CTT'] = df['CTT'].str.replace('Hsi', 'HSI')
    df['CTT'] = df['CTT'].str.replace('Iads', 'I-ADS')
    df['CTT'] = pd.Categorical(df['CTT'], ["W", "Wp", "HSI", "H", "SPY", "SPY-H", "H-ADS", "I-ADS"])
    
    # ... split queries/symbols into different columns
    for qtype in ["Learning", "Testing"]:
        _lst= df[f"{qtype} queries/symbols"].apply(lambda x: [i.split('/') for i in ast.literal_eval(x)])
        df[f"{qtype} queries"]            = _lst.apply(lambda x : np.cumsum([int(i[0]) for i in x])) # resets
        df[f"{qtype} symbols"]            = _lst.apply(lambda x : np.cumsum([int(i[1]) for i in x])) # symbols w/o resets
        df[f"{qtype} cost"]               = _lst.apply(lambda x : np.cumsum([int(i[0])+int(i[1]) for i in x])) # symbols+reset

    # ... and then parsing string with hypotheses sizes as array of integers
    df["HypSize"] = df["HypSize"].apply(lambda x: ast.literal_eval(x))
    df["TC [Symbols]"] = df["EQ [Symbols]"] + df["MQ [Symbols]"]
    df["TC [Resets]"] = df["EQ [Resets]"] + df["MQ [Resets]"]
    df["TC"] = df["TC [Symbols]"] + df["TC [Resets]"]
    df["MQ"] = df["MQ [Symbols]"]+df["MQ [Resets]"]
    df["EQ"] = df["EQ [Symbols]"]+df["EQ [Resets]"]
    

    # ... and then append qSize to HypSize, if the run is successfull 
    df["HypSize"] = df.apply(lambda x: x.HypSize + [x.Qsize] if x.Equivalent=='OK' and len(x.HypSize) < x.Rounds else x.HypSize, axis=1)
    
    # ... and then include #EQs from the single-state model
    df["Testing queries"] = df["Testing queries"].apply(lambda x: [0,*x])
    df["Testing symbols"] = df["Testing symbols"].apply(lambda x: [0,*x])
    df["Testing cost"]    = df["Testing cost"].apply(lambda x: [0,*x])
    
    # ... and then calculate the total number of queries
    df["Total queries"] = df.apply(lambda x: np.add(x["Testing queries"],x["Learning queries"]) if x.Equivalent=='OK' else [], axis=1)
    df["Total symbols"] = df.apply(lambda x: np.add(x["Testing symbols"],x["Learning symbols"]) if x.Equivalent=='OK' else [], axis=1)
    df["Total cost"]    = df.apply(lambda x: np.add(x["Testing cost"],   x["Learning cost"]   ) if x.Equivalent=='OK' else [], axis=1)
    
    # ... and then (FINALLY!) calculate the APFD and AUC for TC
    df_eq = df.query('`Equivalent`=="OK"')
    
    the_cols = ["SUL name","TC"]
    max_eqs = df[the_cols].groupby(["SUL name"]).max().to_dict()

    df["APFD_s1"] = df.apply(lambda x: apfd(x['Total cost'],x['HypSize']) if x.Equivalent=='OK' else -1, axis=1)
    df["AUC_s1"] = df.apply(lambda x: auc_learning(x['Total cost'],x['HypSize']) if x.Equivalent=='OK' else -1, axis=1)

    df["APFD_s2"] = df.apply(lambda x: apfd(x['Total cost'],x['HypSize'],max_nqueries=max_eqs['TC'][(x['SUL name'])]) if x.Equivalent=='OK' else -1, axis=1)
    df["AUC_s2"] = df.apply(lambda x: auc_learning(x['Total cost'],x['HypSize'],max_nqueries=max_eqs['TC'][x['SUL name']]) if x.Equivalent=='OK' else -1, axis=1)

    # to close, return the new dataframe with derived columns
    return df

def _interp_addsorted(alist, datapoints=[]):
    cc_dp = alist.copy()
    for newdp in datapoints:
        if(newdp in cc_dp): continue
        cc_dp = np.insert(cc_dp,np.searchsorted(cc_dp,newdp),newdp)
    return cc_dp

def interp(data: pd.DataFrame.dtypes, col_costs: str, col_hypsizes: str, datapoints=[]):
    df_subset = data.copy()
    df_subset[col_hypsizes+'_withdatapoints']=df_subset[col_hypsizes].apply(lambda x: _interp_addsorted(x,datapoints))
    df_subset[col_costs]=df_subset.apply(lambda x: np.interp(x[col_hypsizes+'_withdatapoints'], x[col_hypsizes], x[col_costs]),axis=1)
    df_subset[col_hypsizes]=df_subset[col_hypsizes+'_withdatapoints']
    df_subset.drop(col_hypsizes+'_withdatapoints',inplace=True,axis=1)
    return df_subset


def VD_A(treatment: List[float], control: List[float]):
    """
    Computes Vargha and Delaney A index
    A. Vargha and H. D. Delaney.
    A critique and improvement of the CL common language
    effect size statistics of McGraw and Wong.
    Journal of Educational and Behavioral Statistics, 25(2):101-132, 2000
    The formula to compute A has been transformed to minimize accuracy errors
    See: http://mtorchiano.wordpress.com/2014/05/19/effect-size-of-r-precision/
    :param treatment: a numeric list
    :param control: another numeric list
    :returns the value estimate and the magnitude

    Code extracted from https://gist.github.com/jacksonpradolima/f9b19d65b7f16603c837024d5f8c8a65
    """
    m = len(treatment)
    n = len(control)

    if m != n:
        raise ValueError("Data d and f must have the same length")

    r = ss.rankdata(treatment + control)
    r1 = sum(r[0:m])

    # Compute the measure
    # A = (r1/m - (m+1)/2)/n # formula (14) in Vargha and Delaney, 2000
    A = (2 * r1 - m * (m + 1)) / (2 * n * m)  # equivalent formula to avoid accuracy errors

    levels = [0.147, 0.33, 0.474]  # effect sizes from Hess and Kromrey, 2004
    magnitude = ["negligible", "small", "medium", "large"]
    scaled_A = (A - 0.5) * 2

    magnitude = magnitude[bisect_left(levels, abs(scaled_A))]
    estimate = A

    return estimate, magnitude

def VD_A_DF(data, val_col: str = None, group_col: str = None, sort=True):
    """
    :param data: pandas DataFrame object
        An array, any object exposing the array interface or a pandas DataFrame.
        Array must be two-dimensional. Second dimension may vary,
        i.e. groups may have different lengths.
    :param val_col: str, optional
        Must be specified if `a` is a pandas DataFrame object.
        Name of the column that contains values.
    :param group_col: str, optional
        Must be specified if `a` is a pandas DataFrame object.
        Name of the column that contains group names.
    :param sort : bool, optional
        Specifies whether to sort DataFrame by group_col or not. Recommended
        unless you sort your data manually.
    :return: stats : pandas DataFrame of effect sizes
    Stats summary ::
    'A' : Name of first measurement
    'B' : Name of second measurement
    'estimate' : effect sizes
    'magnitude' : magnitude

    Code extracted from https://gist.github.com/jacksonpradolima/f9b19d65b7f16603c837024d5f8c8a65
    """

    x = data.copy()
    if sort:
        x[group_col] = Categorical(x[group_col], categories=x[group_col].unique(), ordered=True)
        x.sort_values(by=[group_col, val_col], ascending=True, inplace=True)

    groups = x[group_col].unique()

    # Pairwise combinations
    g1, g2 = np.array(list(it.combinations(np.arange(groups.size), 2))).T

    # Compute effect size for each combination
    ef = np.array([VD_A(list(x[val_col][x[group_col] == groups[i]].values),
                        list(x[val_col][x[group_col] == groups[j]].values)) for i, j in zip(g1, g2)])

    return pd.DataFrame({
        'A': np.unique(data[group_col])[g1],
        'B': np.unique(data[group_col])[g2],
        'estimate': ef[:, 0],
        'magnitude': ef[:, 1]
    })

def sort_vda(df_vda):
    df_vda.estimate = df_vda.estimate.astype(float)
    df_vda['estimate_abs'] = np.abs(df_vda.estimate.astype(float)-0.5)
    df_vda.magnitude = df_vda.apply(lambda x: x['magnitude'] + (f'(A)' if x['estimate']<0.5 else f'(B)'), axis=1)
    return df_vda[['A','B','estimate','magnitude']].set_index(['A','B'])

def _f_s12(x,max_vals):
    d = {}
    d['SUL name'] = x.apply(lambda x: x['SUL name'],axis=1).tolist()
    d['TC_s1'] = x.apply(lambda x: x['TC'],axis=1).tolist()
    d['TC_s2'] = x.apply(lambda x: x['TC']/max_vals['TC_max'][x['SUL name']],axis=1).tolist()
    
    d['APFD_s1'] = x.apply(lambda x: x['APFD_s1'],axis=1).tolist()
    d['APFD_s2'] = x.apply(lambda x: x['APFD_s2'],axis=1).tolist()
    
    return pd.Series(d, index=['SUL name', 'TC_s1', 'APFD_s1', 'TC_s2', 'APFD_s2'])
    
def _f_max(x):
    d = {}
    d['TC_max'] = x['TC'].max()
    d['TC_Symbols_max'] = x['TC [Symbols]'].max()
    return pd.Series(d, index=['TC_max', 'TC_Symbols_max'])

def calc_s12(a_df):
    max_vals = a_df.groupby('SUL name').apply(lambda x: _f_max(x)).to_dict()
    metrics_s12 = a_df.groupby('EquivalenceOracle').apply(lambda x: _f_s12(x,max_vals)).explode(['SUL name', 
                  'TC_s1', 'TC_s2', 'APFD_s1',  'APFD_s2']).reset_index().set_index(['EquivalenceOracle'])
    return metrics_s12

def cartesian(arrays, out=None):
    """
    Generate a Cartesian product of input arrays.
    Source: https://gist.github.com/hernamesbarbara/68d073f551565de02ac5

    Parameters
    ----------
    arrays : list of array-like
        1-D arrays to form the Cartesian product of.
    out : ndarray
        Array to place the Cartesian product in.

    Returns
    -------
    out : ndarray
        2-D array of shape (M, len(arrays)) containing Cartesian products
        formed of input arrays.

    Examples
    --------
    >>> cartesian(([1, 2, 3], [4, 5], [6, 7]))
    array([[1, 4, 6],
           [1, 4, 7],
           [1, 5, 6],
           [1, 5, 7],
           [2, 4, 6],
           [2, 4, 7],
           [2, 5, 6],
           [2, 5, 7],
           [3, 4, 6],
           [3, 4, 7],
           [3, 5, 6],
           [3, 5, 7]])

    """

    arrays = [np.asarray(x) for x in arrays]
    dtype = arrays[0].dtype

    n = np.prod([x.size for x in arrays])
    if out is None:
        out = np.zeros([n, len(arrays)], dtype=dtype)

    #m = n / arrays[0].size
    m = int(n / arrays[0].size)
    out[:,0] = np.repeat(arrays[0], m)
    if arrays[1:]:
        cartesian(arrays[1:], out=out[0:m, 1:])
        for j in range(1, arrays[0].size):
        #for j in xrange(1, arrays[0].size):
            out[j*m:(j+1)*m, 1:] = out[0:m, 1:]
    return out