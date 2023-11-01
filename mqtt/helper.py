import random
from paho.mqtt import client as mqtt_client
from .models import MessageHistory
from datetime import datetime

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

def store(msg):
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