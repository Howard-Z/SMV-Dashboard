from django.shortcuts import render
from .helper import run
import threading

# Create your views here.

#SET TOPICS HERE
topics = ['test', 'test2', 'etc']

#subscribes to above topics and stores them to database
def index(request):
    #todo: build dashboard here
    pass
#threading: starts and maintains MQTT subscription in the background, using run(topics) function from helper
thread = threading.Thread(target=run, name="MQTT_Subscribe", args=[topics])
thread.start()