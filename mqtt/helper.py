import random
from paho.mqtt import client as mqtt_client
from .models import MessageHistory
from datetime import datetime

#topic initialization(tmp)
speed_topic = "speed"
battery_topic = "battery"

global SPEED
SPEED = 0 #init speed to 0

global BATTERY
BATTERY = 0 #init battery to 0

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
    #client.on_connect = on_connect
    client.connect(broker, port)
    return client

#returns global SPEED var for use in dashboard ajax call. avoids writing and pulling from db

#potential idea: create DAQ class with accessors and pass class to front?
#   pros: one var passed, simplifying processes and member functions
#   cons: all data needs to be available to update at once(ie: speed cannot be individually updated)
#   question: how often should different data types be refreshed? ie: speed -> instant, battery -> 1s/5s? reduce system load
def getSpeed():
    global SPEED
    return SPEED
def getBattery():
    global BATTERY
    return BATTERY
def store(msg):
    print(datetime.now())
    if msg.topic == speed_topic:
        global SPEED
        SPEED = int(msg.payload.decode())
    elif msg.topic == battery_topic:
        global BATTERY
        BATTERY = int(msg.payload.decode())
    #TODO: IMPLEMENT STORING FEATURE
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