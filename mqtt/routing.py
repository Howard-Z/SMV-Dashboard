from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from mqtt.consumers import SpeedConsumer
application =[
    path('ws/data', SpeedConsumer.as_asgi()),
]