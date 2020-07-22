from channels.generic.websocket import AsyncWebsocketConsumer
import json
from django.contrib.auth.models import User
import paho.mqtt.client as mqtt
from channels.db import database_sync_to_async
from vehicles.models import Vehicle
import datetime


class DashConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.groupname='dashboard'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self,close_code):

        await self.channel_layer.group_discard(
            self.groupname,
            self.channel_name
        )
    

    async def receive(self, text_data):
        datapoint = json.loads(text_data)
        # Acceleration
        val0X = datapoint['SensorValue3'][0]['valueX']
        val0Y = datapoint['SensorValue3'][0]['valueY']
        val0Z = datapoint['SensorValue3'][0]['valueZ']
        # Magnetometer
        val1X = datapoint['SensorValue3'][1]['valueX']
        val1Y = datapoint['SensorValue3'][1]['valueY']
        val1Z = datapoint['SensorValue3'][1]['valueZ']
        # Gyroscope
        val2X = datapoint['SensorValue3'][2]['valueX']
        val2Y = datapoint['SensorValue3'][2]['valueY']
        val2Z = datapoint['SensorValue3'][2]['valueZ']
        
        # LIDAR
        val0 = datapoint['SensorValue1'][0]['value']
        # Humidity
        val1 = datapoint['SensorValue1'][1]['value']
        # Steering Angle
        val2 = datapoint['SensorValue1'][2]['value']
        # Temperature
        val3 = datapoint['SensorValue1'][3]['value']
        # Speed
        val4 = datapoint['SensorValue1'][4]['value']
        # Altimeter
        val5 = datapoint['SensorValue1'][5]['value']

        # timestamp
        t = datetime.datetime.strptime(datapoint['SensorValue1'][5]['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
        timestamp = t.strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        

        await self.channel_layer.group_send(
            self.groupname,
            {
                'type': 'deprocessing',
                
                'value0X': val0X,
                'value0Y': val0Y,
                'value0Z': val0Z,

                'value1X': val1X,
                'value1Y': val1Y,
                'value1Z': val1Z, 

                'value2X': val2X,
                'value2Y': val2Y,
                'value2Z': val2Z,

                'value0': val0,
                'value1': val1,
                'value2': val2,
                'value3': val3,
                'value4': val4,
                'value5': val5,
                'timestamp': timestamp
            }
        )

        print ('>>>>', text_data)

    async def deprocessing(self, event):
        valOther0X = event['value0X']
        valOther0Y = event['value0Y']
        valOther0Z = event['value0Z']

        valOther1X = event['value1X']
        valOther1Y = event['value1Y']
        valOther1Z = event['value1Z']

        valOther2X = event['value2X']
        valOther2Y = event['value2Y']
        valOther2Z = event['value2Z']
            
        valOther0 = event['value0']
        valOther1 = event['value1']
        valOther2 = event['value2']
        valOther3 = event['value3']
        valOther4 = event['value4']
        valOther5 = event['value5']
        timestampOther = event['timestamp']

        await self.send(text_data=json.dumps(
            {
                'value0X': round(valOther0X, 2), 
                'value0Y': round(valOther0Y, 2), 
                'value0Z': round(valOther0Z, 2),

                'value1X': round(valOther1X, 2), 
                'value1Y': round(valOther1Y, 2), 
                'value1Z': round(valOther1Z, 2), 

                'value2X': round(valOther2X, 2), 
                'value2Y': round(valOther2Y, 2), 
                'value2Z': round(valOther2Z, 2), 
                
                'value0': round(valOther0, 2), 
                'value1': round(valOther1, 2), 
                'value2': round(valOther2, 2), 
                'value3': round(valOther3, 2),
                'value4': round(valOther4, 2), 
                'value5': round(valOther5, 2),
                'timestamp': timestampOther
            }
            ))

class RFIDConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.groupname='rfid'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, close_code):

        await self.channel_layer.group_discard(
            self.groupname,
            self.channel_name
        )
    
    async def receive(self, text_data):
        datapoint = json.loads(text_data)
        print ('>>>>', text_data)
        
        username = 'W2'
        pw = 'DED'
        client = mqtt.Client()
        client.username_pw_set(username, password=pw)
        client.connect("ea-pc165.ei.htwg-konstanz.de", 8883, 60)
        client.loop_start()

        @database_sync_to_async
        def find_user(uname):
            return User.objects.filter(username=uname).first()

        @database_sync_to_async
        def find_vehicle(vname):
            return Vehicle.objects.filter(name=vname).first()
        
        @database_sync_to_async
        def driver_allocate(vehicle, user):
            vehicle.driver = user.username
            vehicle.save()
        
        found_user = await find_user(datapoint['name'])
        found_vehicle = await find_vehicle('Vehicle 1')

        print(found_user)
        print(found_vehicle)
        if found_user != None:
            client.publish("/SysArch/V1/user/confirm", json.dumps({'id': found_user.id}))
            await driver_allocate(found_vehicle, found_user)


    async def deprocessing(self, event):
        pass