import time
import paho.mqtt.client as mqtt
import json
import random

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect

rfid_req = { 'name': 'Aniketos'}

username = 'W2'
pw = 'DED'
client.username_pw_set(username, password=pw)
client.connect("ea-pc165.ei.htwg-konstanz.de", 8883, 60)

client.loop_start()

while True:
    time.sleep(10)
    client.publish("/SysArch/V1/user/rfidrequest", json.dumps(rfid_req))
    print('Data sent...')