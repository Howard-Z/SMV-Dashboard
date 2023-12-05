from django.shortcuts import render
from django.http.response import JsonResponse
from .helper import run
from .models import Trip
import threading
import json
from datetime import datetime
from django.shortcuts import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'mqtt/dashboard.html')

def map(request):
    return render(request, 'mqtt/map.html')

def dash_admin(request):
    if request.method == "POST":
        data = json.loads(request.body)
        match data['feature']:
            case "increment_trip":
                Trip.objects.last().active = False
                Trip.objects.create(name=data['data'], date_created=datetime.now(), active=True)
        return JsonResponse({"status": "200"})
    else:
        recent_trip = Trip.objects.last()
        return render(request, 'mqtt/dashboard_admin.html', {
            "trip": recent_trip
        })
#threading: starts and maintains MQTT subscription in the background, using run(topics) function from helper
thread = threading.Thread(target=run, name="MQTT_Subscribe", daemon=True)
thread.start()
