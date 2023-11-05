from django.shortcuts import render
from django.http.response import JsonResponse
from .helper import run, getSpeed, getBattery
import threading

# Create your views here.

#SET TOPICS HERE
topics = ['test', 'test2', 'etc', '/hello', 'speed']

#subscribes to above topics and stores them to database
def index(request):
    #todo: build dashboard here
    return render(request, 'mqtt/dashboard.html')

def ajax_speed(request):
    battery = getBattery()
    if battery < 10:
        status = "alert"
    elif battery < 20:
        status = "warn"
    else:
        status = "good"
    return JsonResponse({"speed": getSpeed(), "battery": {"level": getBattery(), "status": status}})

def map(request):
    return render(request, 'mqtt/map.html')
#threading: starts and maintains MQTT subscription in the background, using run(topics) function from helper
thread = threading.Thread(target=run, name="MQTT_Subscribe", args=[topics])
thread.start()