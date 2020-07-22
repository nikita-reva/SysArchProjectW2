import paho.mqtt.client as mqtt
import json
import requests
import websocket
import random, time

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    # client.subscribe("/SysArch/V1/user/#")
    client.subscribe("/SysArch/V1/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    topic = msg.topic
    massage_decode = str(msg.payload.decode("utf-8", "ignore"))
    data_in = json.loads(massage_decode)
    data_db = { 
        "name": data_in['SensorValue1'][3]['name'],
        "timestamp": 21487388932,
        "value": data_in['SensorValue1'][3]['value']
        }
    print(topic)
    print(massage_decode)
    # r = requests.post('http://127.0.0.1:8000/data-acquisition/sensordata/', json=data_db)
    # print(r.status_code)
    # print(r.text)
    ws1.send(json.dumps(data_in))

    with open('data.json', 'w') as file:
        file.write(json.dumps(data_in))

def on_message_request(client, userdata, msg):
    topic = msg.topic
    massage_decode = str(msg.payload.decode("utf-8", "ignore"))
    data_in = json.loads(massage_decode)
    print(topic)
    print(massage_decode)
    ws2.send(json.dumps(data_in))

def on_message_confirm(client, userdata, msg):
    topic = msg.topic
    massage_decode = str(msg.payload.decode("utf-8", "ignore"))
    data_in = json.loads(massage_decode)
    print(topic)
    print(massage_decode)



client = mqtt.Client()
ws1 = websocket.WebSocket()
ws2 = websocket.WebSocket()

client.on_connect = on_connect
client.message_callback_add('/SysArch/V1/sensor', on_message)
client.message_callback_add('/SysArch/V1/com2/web', on_message_request)
client.message_callback_add('/SysArch/V1/user/confirm', on_message_confirm)

username = 'W2'
pw = 'DED'
client.username_pw_set(username, password=pw)

client.connect("ea-pc165.ei.htwg-konstanz.de", 8883, 60)
ws1.connect('ws://localhost:8000/ws/polData/')
ws2.connect('ws://localhost:8000/ws/rfid/')

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()