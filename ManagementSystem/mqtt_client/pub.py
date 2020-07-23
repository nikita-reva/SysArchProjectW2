import time
import paho.mqtt.client as mqtt
import json
import random
from datetime import datetime

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect

rfid_req1 = { 
    'timestamp': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'),
    'tokenID': 'blabla',
    'login': True,
    }
rfid_req2 = { 
    'timestamp': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f'),
    'tokenID': 'blabla',
    'login': False,
    }

username = 'W2'
pw = 'DED'
client.username_pw_set(username, password=pw)
client.connect("ea-pc165.ei.htwg-konstanz.de", 8883, 60)

client.loop_start()

while True:
    time.sleep(10)
    client.publish("/SysArch/V1/com2/web", json.dumps(rfid_req1))
    print('Data sent...')
    time.sleep(10)
    client.publish("/SysArch/V1/com2/web", json.dumps(rfid_req2))
    print('Data sent...')    