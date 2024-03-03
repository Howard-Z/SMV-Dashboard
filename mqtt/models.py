from django.db import models
import sys
from datetime import datetime
sys.path.append("..")
# Create your models here.
    
class Trip(models.Model):
    name = models.CharField(max_length=128, default="", blank="", null="")
    active = models.BooleanField(default=False)
    date_created = models.DateField()
    start = models.DateTimeField()
    stop = models.DateTimeField( default=datetime.fromtimestamp(0), blank=datetime.fromtimestamp(0), null=datetime.fromtimestamp(0))

    def __str__(self):
        return f"{self.id}: {self.name}"
#set: DAQMessage
class SpeedData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = " Speed Data" 
class Location(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    longitude = models.DecimalField(max_digits=11, decimal_places=7)
    latitude = models.DecimalField(max_digits=11, decimal_places=7)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = " Location Data" 
#
# POWER DATA
#

class CurrentData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "  Current Data" 
class VoltageData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "  Voltage Data" 
class PowerData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "  Power Data" 

class Temperature(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "  Temperature Data" 
#set: steeringMessage
class Switch_EncodingData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "   Switch Encoding Data" 


class S_Error_StatusData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "   S Error Status Data" 

#set: motorMessage
class RPMData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "    RPM Data" 
class Motor_StateData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "    Motor State Data" 
class CruiseData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "    Cruise Data" 
class M_Error_StatusData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "    M Error Status Data" 
class ThrottleData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "    Throttle Data" 
class BrakeData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "    Brake Data" 

class Meter_CountData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    data = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
    class Meta:
        verbose_name_plural = "    Meter Count Data" 

#extra data
class MessageHistory(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE, default=None, blank=None)
    topic = models.CharField(max_length=128)
    message = models.TextField()
    date = models.DateTimeField()
    def __str__(self):
        return self.topic
class MQTTError(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE, default=None, blank=None)
    module = models.CharField(max_length=30, choices = (("mqtt", "mqtt"), ("ws", "ws")))
    event = models.CharField(max_length=30, choices = (("connect", "connect"), ("disconnect", "disconnect"), ("receive_message", "receive_message")))
    message = models.TextField()
    error = models.BooleanField()
    time = models.DateTimeField()