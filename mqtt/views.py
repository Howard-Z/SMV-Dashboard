from django.shortcuts import render
from django.http.response import JsonResponse
from .helper import run, getSpeed, getBattery, getLocation
import threading
import time
# Create your views here.

#SET TOPICS HERE
#topics: Bear_1
topics = ["/Bear_1/RPM","/Bear_1/Motor_State","/Bear_1/Cruise","/Bear_1/M_Error_Status","/Bear_1/Throttle","/Bear_1/Brake", "/Bear_1/Meter_Count"]

#topics: Bear 2
topics += ["/Bear_2/RPM","/Bear_2/Motor_State","/Bear_2/Cruise","/Bear_2/M_Error_Status","/Bear_2/Throttle","/Bear_2/Brake", "/Bear_2/Meter_Count"]

#topics: Power_Control
topics += ["/Power_Control/Current","/Power_Control/Voltage","/Power_Control/Power","/Power_Control/Energy","/Power_Control/T1","/Power_Control/T2", "/Power_Control/T3", "/Power_Control/P_Error_Status"]

#topic: Steering_Wheel
topics += ["/Steering_Wheel/Switch_Encoding", "Steering_Wheel/S_Error_Status"]

#topic: DAQ
topics += ["/DAQ/Longitude", "/DAQ/Latitude", "/DAQ/Speed"]

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
    return JsonResponse({"speed": getSpeed()})
def ajax_battery(request):
    battery = getBattery()
    if battery < 10:
        status = "alert"
    elif battery < 20:
        status = "warn"
    else:
        status = "good"
    return JsonResponse({"level": battery, "status": status})
def ajax_location(request):
    long, lat = getLocation()
    return JsonResponse({"long": long, "lat": lat})

def map(request):
    return render(request, 'mqtt/map.html')

#threading: starts and maintains MQTT subscription in the background, using run(topics) function from helper
thread = threading.Thread(target=run, name="MQTT_Subscribe", args=[topics], daemon=True)
thread.start()
print(True)