import random
from paho.mqtt import client as mqtt_client
from .models import MessageHistory, Trip, MQTTError
from datetime import datetime
import time
from .topics import topics_list as topics
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

LOCATION = [0,0,0]

broker = 'apt.howard-zhu.com'
port = 1883
# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-{random.randint(0, 100)}'
# username = 'homeassistant'
# password = 'gelaithah9ajiecohlahteigeizeeCuNeichoow5thaaquiPhaCh5quu6zoo0ael'
def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            MQTTError.objects.create(module='mqtt', event='connect', message='connected', error=False, time=datetime.now())
        else:
            MQTTError.objects.create(module='mqtt', event='connect', message=f"Failed to connect, return code {rc}, client: {client}\n", error=True, time=datetime.now())
    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    print("connected")
    return client

#returns global SPEED var for use in dashboard ajax call. avoids writing and pulling from db

#potential idea: create DAQ class with accessors and pass class to front?
#   pros: one var passed, simplifying processes and member functions
#   cons: all data needs to be available to update at once(ie: speed cannot be individually updated)
#   question: how often should different data types be refreshed? ie: speed -> instant, battery -> 1s/5s? reduce system load

def store(msg):
    channel_layer = get_channel_layer()
    topics[msg.topic]['model'].objects.create(date=datetime.now(), data=int(msg.payload.decode()), trip=Trip.objects.last()) #update model
    if str(msg.topic) != "/DAQ/Latitude" and str(msg.topic) != "/DAQ/Longitude":
        #do NOT deal with long/lat here. need to implement separate feature to store it
        pass
    else:
        #TODO: SEND TO TEAM VIEW ALWAYS, except for lat/long data
        async_to_sync(channel_layer.group_send)("teamdata", {"type": f"team.notif", "module": f"{topics[msg.topic]['name']}", "content": int(msg.payload.decode()), "error": False})
    if str(msg.topic) == "/DAQ/Speed" or str(msg.topic) == "/Power_Control/Energy":
        #send to dashboard ONLY for speed and energy(to avoid sending non-relevant data)
        async_to_sync(channel_layer.group_send)("speed", {"type": f"data.notif", "module": f"{topics[msg.topic]['name']}", "content": int(msg.payload.decode()), "error": False})

    MessageHistory.objects.create(topic=msg.topic, message = msg.payload.decode(), date=datetime.now(), trip=Trip.objects.last())
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

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