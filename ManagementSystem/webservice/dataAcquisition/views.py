from django.shortcuts import render

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Sensor
from .serializers import SensorSerializer

class SensorView(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

