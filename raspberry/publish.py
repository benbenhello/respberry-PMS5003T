#**************************************************** 
# Import Package                                                                           
#**************************************************** 

import time
import datetime
import paho.mqtt.client as paho
import json
import ssl

import lib.G5_module as G5_m

# Set AWS Config
connflag = False

#**************************************************** 
# Set AWS Connection                                                   
#**************************************************** 

def on_connect(client, userdata, flags, rc):
    global connflag
    connflag = True
    print("Connection returned result: " + str(rc) )

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

mqttc = paho.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message

awshost = "a2gha0fkz5hg2j-ats.iot.us-west-2.amazonaws.com"
awsport = 8883
clientId = "sensorData"
thingName = "sensorData"
caPath = "./AWS_IoT/AmazonRootCA1.pem"
certPath = "./AWS_IoT/560a5505f3-certificate.pem.crt"
keyPath = "./AWS_IoT/560a5505f3-private.pem.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
mqttc.connect(awshost, awsport, keepalive=60)
mqttc.loop_start()

#**************************************************** 
# Publish AWS                                                  
#**************************************************** 

while True:

    if connflag == True:
        print("success")
        mqttc.publish("topic/test", json.dumps({"temperature": "25",
                                                "humidity": "10",
                                                "PM1.0": "10",
                                                "PM2.5": "10",
                                                "PM10": "10"
        }), qos=1)
    else:
        print("waiting for connection...")
    time.sleep(5)
