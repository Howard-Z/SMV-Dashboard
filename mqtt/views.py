from django.shortcuts import render
from django.http.response import JsonResponse, Http404
from .helper import run, publish
from .models import Trip
import threading
import json
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def index(request):
    return render(request, 'mqtt/dashboard.html')

def map(request):
    #temp map view 
    return render(request, 'mqtt/map.html')
def chart(request):
    return render(request, 'mqtt/chart.html')
def dash_admin(request):
    if request.method == "POST":
        data = json.loads(request.body)
        match data['feature']:
            case "increment_trip":
                if data['data'] is not None:
                    Trip.objects.last().active = False
                    Trip.objects.create(name=data['data'], date_created=datetime.now(), active=True)
            case "publish_mqtt":
                data = json.loads(data['data'])
                publish(topic=data['topic'], message=data['message'])
        return JsonResponse({"status": "200"})
    else:
        recent_trip = Trip.objects.last()
        return render(request, 'mqtt/dashboard_admin.html', {
            "trip": recent_trip,
        })
    
def team_view(request):
    return render(request, 'mqtt/team_dash.html')


def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("dash_admin"), status=302)
        else:
            return render(request, "mqtt/dashboard_admin.html", {
                "message": "Invalid username and/or password."
            })
    else:
        raise Http404
    
#threading: starts and maintains MQTT subscription in the background, using run(topics) function from helper
thread = threading.Thread(target=run, name="MQTT_Subscribe", daemon=True)
thread.start()
