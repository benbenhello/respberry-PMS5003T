#**************************************************** 
# Import Package                                                                           
#**************************************************** 

import pigpio
import subprocess
import logging
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

## initial PIGPIO library ##
(s, process) = subprocess.getstatusoutput('sudo pidof pigpiod')

if s:
    print("pigpiod was not running")
    subprocess.getstatusoutput('sudo pigpiod')
    time.sleep(0.1)

if not s:
    print("pigpio is running, process ID is %s", process)

pi = pigpio.pi()
print("start to sense environment")

#**************************************************** 
# Publish AWS                                                  
#**************************************************** 

while True:

    print("==================================")
    
    ########## PM2.5 Part ##########
    try:
        pi.bb_serial_read_close(14)
    except Exception:
        pass

    print("G5 port has already closed")

    try:
        pi.bb_serial_read_open(14, 9600)
        time.sleep(1)
        (status, pm25_raw_data) = pi.bb_serial_read(14)
        if status:
            print("G5 read data successfully")
            hex_data = G5_m.bytes2hex(pm25_raw_data)
            global Temp, Hum, Pm1, Pm25, Pm10
            (check, pm1, pm25, pm10, temp, hum) = G5_m.read_data(hex_data)
            if check:
                print("@@ PM1.0 DATA:", str(pm1))
                print("@@ PM2.5 DATA:", str(pm25))
                print("@@ PM10 DATA:", str(pm10))
                print("@@ TEMP:", str(temp))
                print("@@ HUM:", str(hum))
                (Temp, Hum, Pm1, Pm25, Pm10) = (temp, hum, pm1, pm25, pm10)
            else:
                print("G5 read data failed")

    except Exception as e:
        print("G5 port open failed, error msg: %s", e)

    try:
        pi.bb_serial_read_close(14)
    except Exception:
        pass

    print("G5 port close successfully")

    ##############################


    if connflag == True:
        print("success")
        mqttc.publish("topic/test", json.dumps({"temperature": Temp,
                                                "humidity": Hum,
                                                "PM1.0": Pm1,
                                                "PM2.5": Pm25,
                                                "PM10": Pm10
        }), qos=1)
    else:
        print("waiting for connection...")
    time.sleep(5)
