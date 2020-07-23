import time
import paho.mqtt.client as mqtt
import json
import random

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

client = mqtt.Client()
client.on_connect = on_connect

username = 'W2'
pw = 'DED'
client.username_pw_set(username, password=pw)
client.connect("ea-pc165.ei.htwg-konstanz.de", 8883, 60)

client.loop_start()

while True:
    time.sleep(2)
    client.publish("/SysArch/V1/sensor", json.dumps(
            {
                "SensorValue3": 
                    [
                        {
                            "timestamp": "2020-07-22 13:46:58.042905", 
                            "valueZ": random.randint(-50, 50), 
                            "name": "Acceleration", 
                            "valueY": random.randint(-50, 50), 
                            "valueX": random.randint(-50, 50), 
                        }, 
                        {
                            "timestamp": "2020-07-22 13:46:58.042905", 
                            "valueZ": random.randint(-5000, 5000), 
                            "name": "Magnetometer", 
                            "valueY": random.randint(-5000, 5000),  
                            "valueX": random.randint(-5000, 5000), 
                        }, 
                        {
                            "timestamp": "2020-07-22 13:46:58.042905", 
                            "valueZ": random.randint(-100, 100), 
                            "name": "Gyro", 
                            "valueY": random.randint(-100, 100), 
                            "valueX": random.randint(-100, 100)
                        }
                    ], 
                    "SensorValue1": 
                    [
                        {
                            "timestamp": "2020-07-22 13:46:58.042905", 
                            "name": "LIDAR", 
                            "value": random.randint(1, 50)
                        }, 
                        {
                            "timestamp": "2020-07-22 13:46:58.042905", 
                            "name": "Humidity", 
                            "value": random.randint(0, 10)
                        }, 
                        {
                            "timestamp": "2020-07-22 13:46:58.042905", 
                            "name": "SteeringAngle", 
                            "value": random.randint(0, 180)
                        }, 
                        {
                            "timestamp": "2020-07-22 13:46:58.042905", 
                            "name": "Temperature", 
                            "value": random.randint(1, 50)
                        }, 
                        {
                            "timestamp": "2020-07-22 13:46:58.042905", 
                            "name": "Speed", 
                            "value": random.randint(1, 200)
                        }, 
                        {
                            "timestamp": "2020-07-22 13:46:58.042905", 
                            "name": "Altimeter", 
                            "value": random.randint(300, 400)
                        }
                    ]
                }
            ))
    print('Data sent...')