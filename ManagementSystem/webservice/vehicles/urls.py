from django.urls import path
from .views import VehicleListView, VehicleDetailView
from . import views

urlpatterns = [
        path('', VehicleListView.as_view(), name='vehicles-home'),
        path('vehicle/<int:pk>/', VehicleDetailView.as_view(), name='vehicle-detail'),
]