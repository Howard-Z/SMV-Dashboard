from django.shortcuts import render
from django.http.response import JsonResponse
from .helper import run
import threading
import time
from django.shortcuts import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'mqtt/dashboard.html')

def map(request):
    return render(request, 'mqtt/map.html')

def dash_admin(request):
    return render(request, 'mqtt/dashboard_admin.html')
#threading: starts and maintains MQTT subscription in the background, using run(topics) function from helper
thread = threading.Thread(target=run, name="MQTT_Subscribe", daemon=True)
thread.start()
