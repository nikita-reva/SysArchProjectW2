from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Vehicle

class VehicleListView(ListView):
    model = Vehicle
    template_name = 'vehicles/vehicles.html' # <app>/<model>_<viewtype>.html
    context_object_name = 'vehicles'
    ordering = ['id']

class VehicleDetailView(DetailView):
    model = Vehicle