from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from mqtt.consumers import DashboardConsumer
application =[
    path('ws/dashboard', DashboardConsumer.as_asgi()),
]