import random
from paho.mqtt import client as mqtt_client
from .models import MessageHistory, Trip, MQTTError
from datetime import datetime
import time
from .topics import topics_list as topics
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import os

LOCATION = [0,0,0]

broker = '128.97.3.48'
port = 1883
# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-{random.randint(0, 100)}'
username = 'smv'
password = os.environ.get("MQTT_PW")
def connect_mqtt(client_id=client_id) -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            MQTTError.objects.create(module='mqtt', event='connect', message='connected', error=False, time=datetime.now(), trip=Trip.objects.last())
        else:
            MQTTError.objects.create(module='mqtt', event='connect', message=f"Failed to connect, return code {rc}, client: {client}\n", error=True, time=datetime.now(), trip=Trip.objects.last())
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def store(msg):
    channel_layer = get_channel_layer()
    #update associated model
    topics[msg.topic]['model'].objects.create(date=datetime.now(), data=int(msg.payload.decode()), trip=Trip.objects.last()) 

    if str(msg.topic) != "/DAQ/Latitude" and str(msg.topic) != "/DAQ/Longitude":
        #do NOT deal with long/lat here. need to implement separate feature to store it
        pass
    else:
        #send to team view always, except for lat/long data
        async_to_sync(channel_layer.group_send)("teamdata", {"type": f"team.notif", "module": f"{topics[msg.topic]['name']}", "content": int(msg.payload.decode()), "error": False})
    if str(msg.topic) in ['/DAQ/Speed', "/Power_Control/Voltage", "/Power_Control/Current"]:
        #send to dashboard ONLY for speed and energy(to avoid sending non-relevant data)
        async_to_sync(channel_layer.group_send)("speed", {"type": f"data.notif", "module": f"{topics[msg.topic]['name']}", "content": int(msg.payload.decode()), "error": False})


def subscribe(topic, client: mqtt_client):
    def on_message(client, userdata, msg):
        store(msg)
    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    for topic in topics:
        subscribe(topic, client)
    client.loop_forever()

def publish(topic, message):
    client = connect_mqtt(client_id=f'subscribe-{random.randint(0, 1000)}')
    client.publish(topic, message)
