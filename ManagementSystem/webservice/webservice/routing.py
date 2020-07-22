from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from django.urls import path
from vehicles import consumer

websocket_urlPattern=[
    path('ws/polData/', consumer.DashConsumer),
    path('ws/rfid/', consumer.RFIDConsumer),
]

application=ProtocolTypeRouter({
    'websocket':AuthMiddlewareStack(URLRouter(websocket_urlPattern))
})