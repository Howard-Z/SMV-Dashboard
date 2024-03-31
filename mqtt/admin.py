from django.contrib import admin
from .models import MessageHistory, SpeedData, Location, Trip, Blinker
from .models import RPMData, Motor_StateData, CruiseData, M_Error_StatusData, ThrottleData, BrakeData, Meter_CountData, MQTTError, Gyro_x, Gyro_y, Gyro_z, Magnetometer, Accel

#columns
class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ("id", "topic", "date", "trip")
class MQTTErrorAdmin(admin.ModelAdmin):
    list_display = ("trip", "module", "event", "time", "error")
class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "trip", "date", "latitude", "longitude")
# Register your models here.
admin.site.register(MQTTError, MQTTErrorAdmin)
admin.site.register(Blinker)
admin.site.register(RPMData)
admin.site.register(Magnetometer)
admin.site.register(Motor_StateData)
admin.site.register(CruiseData)
admin.site.register(M_Error_StatusData)
admin.site.register(ThrottleData)
admin.site.register(Meter_CountData)
admin.site.register(BrakeData)
admin.site.register(Gyro_x)
admin.site.register(Gyro_y)
admin.site.register(Gyro_z)
admin.site.register(Accel)
admin.site.register(MessageHistory, MessageHistoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Trip)
admin.site.register(SpeedData)

