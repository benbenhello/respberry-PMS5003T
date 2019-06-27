import time  
import datetime  
import paho.mqtt.client as paho  
import json  
import ssl  
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt




connflag = False
start_time = 0
temperature = []
humidity = []
PM25 = []
PM1 = []
PM10 = []
t = []
a = 0

def plot(data,data2,name,name2,file):
    plot_df = pd.DataFrame(
        {name: data,
         name2: data2
        }
    )
    plot = sns.factorplot(data = plot_df, x=name, y=name2, ci = None)
    plot.savefig(file)

def on_connect(client, userdata, flags, rc):  
    global connflag
    connflag = True
    print("Connection returned result: " + str(rc) )

def on_message(client, userdata, msg): 
    now_time = time.time()
    print(msg.topic+" "+str(msg.payload))
    data = json.loads(msg.payload)
    #寫入data.json
    with open('../data.json', 'w') as outfile:
        json.dump(data, outfile)
    #取json的data(用來畫圖)
    humidity.append(data['humidity'])
    temperature.append(data['temperature'])
    PM25.append(data['PM2.5'])
    PM1.append(data['PM1.0'])
    PM10.append(data['PM10'])
    t.append(round(now_time - start_time))

    # print(humidity) #25
    # print(PM25)
    # print(t)
    #畫圖
    plot(t,humidity,"time","humidity","../public/images/humidity.jpg")
    plot(t,temperature,"time","temperature","../public/images/temperature.jpg")
    plot(t,PM25,"time","PM2.5","../public/images/pm25.jpg")
    plot(t,PM1,"time","PM1.0","../public/images/pm1.jpg")
    plot(t,PM10,"time","PM10","../public/images/pm10.jpg")


mqttc = paho.Client()  
mqttc.on_connect = on_connect  
mqttc.on_message = on_message

awshost = "a2gha0fkz5hg2j-ats.iot.us-west-2.amazonaws.com"  
awsport = 8883
clientId = "sensorData"  
thingName = "sensorData"  
caPath = "./AmazonRootCA1.pem"  
certPath = "./560a5505f3-certificate.pem.crt"  
keyPath = "./560a5505f3-private.pem.key"

mqttc.tls_set(caPath, certfile=certPath, keyfile=keyPath, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)  
mqttc.connect(awshost, awsport, keepalive=60)  
mqttc.loop_start()

start_time = time.time()
while True:
    if connflag == True:
        print("success")
        
        mqttc.subscribe("topic/test",1)
    else:
        print("waiting for connection...")
    time.sleep(1)
