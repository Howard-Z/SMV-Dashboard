from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from mqtt.consumers import DashboardConsumer, TeamConsumer
application =[
    path('ws/dashboard', DashboardConsumer.as_asgi()),
    path('ws/teamview', TeamConsumer.as_asgi())
]