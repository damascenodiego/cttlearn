#!/bin/sh

CTT_LEARNING="java -jar ./bin/cttlearning.jar"
EXTRA_STATES=0


$CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/GnuTLS_3.3.12_client_full.dot" # default W method (by LearnLib)
$CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/GnuTLS_3.3.12_client_full.dot" -eq soucha_w # W method (by Soucha)

# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/Bankcard/1_learnresult_MasterCard_fix.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/Bankcard/10_learnresult_MasterCard_fix.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/Bankcard/4_learnresult_MAESTRO_fix.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/Bankcard/4_learnresult_PIN_fix.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/Bankcard/4_learnresult_SecureCode Aut_fix.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/Bankcard/ASN_learnresult_MAESTRO_fix.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/Bankcard/ASN_learnresult_SecureCode Aut_fix.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/Bankcard/learnresult_fix.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/Bankcard/Rabo_learnresult_MAESTRO_fix.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/Bankcard/Rabo_learnresult_SecureCode_Aut_fix.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/Bankcard/Volksbank_learnresult_MAESTRO_fix.dot"

# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/FromRhapsodyToDezyne/model1.dot" 
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/FromRhapsodyToDezyne/model2.dot" 
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/FromRhapsodyToDezyne/model3.dot" 
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/FromRhapsodyToDezyne/model4.dot" 

# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/ActiveMQ/invalid.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/ActiveMQ/non_clean.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/ActiveMQ/simple.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/ActiveMQ/single_client.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/ActiveMQ/two_client_will_retain.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/emqtt/invalid.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/emqtt/non_clean.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/emqtt/simple.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/emqtt/single_client.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/emqtt/two_client_same_id.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/emqtt/two_client_will_retain.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/emqtt/two_client.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/hbmqtt/invalid.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/hbmqtt/non_clean.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/hbmqtt/simple.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/hbmqtt/single_client.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/hbmqtt/two_client_will_retain.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/hbmqtt/two_client.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/mosquitto/invalid.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/mosquitto/mosquitto.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/mosquitto/non_clean.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/mosquitto/single_client.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/mosquitto/two_client_same_id.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/mosquitto/two_client_will_retain.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/mosquitto/two_client.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/VerneMQ/invalid.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/VerneMQ/non_clean.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/VerneMQ/simple.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/VerneMQ/single_client.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/VerneMQ/two_client_same_id.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/VerneMQ/two_client_will_retain.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/MQTT/VerneMQ/two_client.dot"

# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/QUICprotocol/QUICprotocolwith0RTT.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/QUICprotocol/QUICprotocolwithout0RTT.dot"

# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/SSH/BitVise.dot.fixed"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/SSH/DropBear.dot.fixed"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/SSH/OpenSSH.dot.fixed"

# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TCP/TCP_FreeBSD_Client.dot.fixed"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TCP/TCP_FreeBSD_Server.dot.fixed"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TCP/TCP_Linux_Client.dot.fixed"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TCP/TCP_Linux_Server.dot.fixed"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TCP/TCP_Windows8_Client.dot.fixed"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TCP/TCP_Windows8_Server.dot.fixed"

# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/GnuTLS_3.3.12_client_full.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/GnuTLS_3.3.12_client_regular.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/GnuTLS_3.3.12_server_full.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/GnuTLS_3.3.12_server_regular.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/GnuTLS_3.3.8_client_full.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/GnuTLS_3.3.8_client_regular.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/GnuTLS_3.3.8_server_full.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/GnuTLS_3.3.8_server_regular.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/miTLS_0.1.3_server_regular.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/NSS_3.17.4_client_full.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/NSS_3.17.4_client_regular.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/NSS_3.17.4_server_regular.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/OpenSSL_1.0.1g_client_regular.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/OpenSSL_1.0.1g_server_regular.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/OpenSSL_1.0.1j_client_regular.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/OpenSSL_1.0.1j_server_regular.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/OpenSSL_1.0.1l_client_regular.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/OpenSSL_1.0.1l_server_regular.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/OpenSSL_1.0.2_client_full.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/OpenSSL_1.0.2_client_regular.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/OpenSSL_1.0.2_server_regular.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/RSA_BSAFE_C_4.0.4_server_regular.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/TLS/RSA_BSAFE_Java_6.1.1_server_regular.dot"

# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/Xray_system_PCS/learnresult1.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/Xray_system_PCS/learnresult2.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/Xray_system_PCS/learnresult3.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/Xray_system_PCS/learnresult4.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/Xray_system_PCS/learnresult5.dot"
# $CTT_LEARNING -es $EXTRA_STATES -sul "./benchmarks/Xray_system_PCS/learnresult6.dot"