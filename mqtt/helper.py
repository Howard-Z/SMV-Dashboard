import random
from paho.mqtt import client as mqtt_client
from .models import MessageHistory
from datetime import datetime
import time
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

#topic initialization(tmp)
speed_topic = "/DAQ/Speed"
battery_topic = "/Power_Control/Energy" #check later
long_topic = "/DAQ/Longitude"
lat_topic = "/DAQ/Latitude"

SPEED, BATTERY = 0, 0 #init speed to 0
LOCATION = [0,0,0]

broker = 'apt.howard-zhu.com'
port = 1883
# Generate a Client ID with the subscribe prefix.
client_id = f'subscribe-{random.randint(0, 100)}'
username = 'homeassistant'
password = 'gelaithah9ajiecohlahteigeizeeCuNeichoow5thaaquiPhaCh5quu6zoo0ael'
def connect_mqtt() -> mqtt_client:
    # def on_connect(client, userdata, flags, rc):
    #     if rc == 0:
    #         print("Connected to MQTT Broker!")
    #     else:
    #         print(f"Failed to connect, return code {rc}, client: {client}\n")
    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    # client.on_connect = on_connect
    client.connect(broker, port)
    return client

#returns global SPEED var for use in dashboard ajax call. avoids writing and pulling from db

#potential idea: create DAQ class with accessors and pass class to front?
#   pros: one var passed, simplifying processes and member functions
#   cons: all data needs to be available to update at once(ie: speed cannot be individually updated)
#   question: how often should different data types be refreshed? ie: speed -> instant, battery -> 1s/5s? reduce system load

def store(msg):
    channel_layer = get_channel_layer()
    if msg.topic == speed_topic:
        async_to_sync(channel_layer.group_send)("speed", {"type": "data.notif", "module": "daq_speed", "content": int(msg.payload.decode())})
    elif msg.topic == battery_topic:
        async_to_sync(channel_layer.group_send)("speed", {"type": "data.notif", "module": "power_energy", "content": int(msg.payload.decode())})
    elif msg.topic == long_topic:
        LOCATION[0] = int(msg.payload.decode())
        LOCATION[1] = 0
    elif msg.topic == lat_topic:
        LOCATION[1] = int(msg.payload.decode())
        LOCATION[2] = 1

    #TODO: IMPLEMENT SORTING/STORING FEATURE
    MessageHistory.objects.create(topic=msg.topic, message = msg.payload.decode(), date=datetime.now())
    print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

def subscribe(topic, client: mqtt_client):
    def on_message(client, userdata, msg):
        store(msg)
    client.subscribe(topic)
    client.on_message = on_message

def run(topics):
    client = connect_mqtt()
    for topic in topics:
        subscribe(topic, client)
    client.loop_forever()

#accessor functions
def getSpeed():
    global SPEED
    return SPEED
def getBattery():
    global BATTERY
    return BATTERY
def getLocation():
    while(LOCATION[2] != 1):
        time.sleep(1)
        getLocation()
    #returns in format: long, lat
    return LOCATION[0], LOCATION[1]
