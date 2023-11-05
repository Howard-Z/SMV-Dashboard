from django.db import models
import sys
sys.path.append("..")
# Create your models here.
    
class Trip(models.Model):
    name = models.CharField(max_length=128, default="", blank="", null="")
    active = models.BooleanField(default=False)
    date_created = models.DateField()
    def __str__(self):
        return f"{self.id}: {self.name}"
#set: DAQMessage
class SpeedData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    speed = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
class Location(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    longitude = models.DecimalField(max_digits=11, decimal_places=7)
    longitude = models.DecimalField(max_digits=11, decimal_places=7)
    date = models.DateTimeField()
class CurrentData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    current = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
#set: powerMessage
class VoltageData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    voltage = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
class PowerData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    power = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
class EnergyData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    energy = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
class T1Data(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    t1 = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
class T2Data(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    t1 = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()

class T3Data(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    t1 = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
#set: steeringMessage
class Switch_EncodingData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    Switch_Encoding = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()

#set: motorMessage
class RPMData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    rpm = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
class Motor_StateData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    Motor_State = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
class CruiseData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    cruise = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
class M_Error_StatusData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    M_Error_Status = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
class ThrottleData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    throttle = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()
class BrakeData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    brake = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()

class Meter_CountData(models.Model):
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    Meter_Count = models.DecimalField(max_digits=6, decimal_places=3)
    date = models.DateTimeField()

class MessageHistory(models.Model):
    topic = models.CharField(max_length=128)
    message = models.TextField()
    date = models.DateTimeField()
    def __str__(self):
        return self.topic