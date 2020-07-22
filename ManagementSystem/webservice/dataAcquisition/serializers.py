from rest_framework import serializers, permissions
from .models import Sensor

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['name', 'timestamp', 'value']