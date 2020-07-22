import paho.mqtt.client as mqtt
import json
import requests
import websocket
import random, time

def on_connect(client, userdata, flags, rc):
    print("Client 1: Connected with result code "+str(rc))

    client.subscribe("/SysArch/V1/com2/web")

def on_message(client, userdata, msg):
    topic = msg.topic
    massage_decode = str(msg.payload.decode("utf-8", "ignore"))
    data_in = json.loads(massage_decode)
    print(topic)
    print(massage_decode)

client = mqtt.Client()

ws = websocket.WebSocket()

client.on_connect = on_connect
client.on_message = on_message

username = 'W2'
pw = 'DED'
client.username_pw_set(username, pw)

client.connect("ea-pc165.ei.htwg-konstanz.de", 8883, 60)

ws.connect('ws://localhost:8000/ws/rfid/')

client.loop_forever()