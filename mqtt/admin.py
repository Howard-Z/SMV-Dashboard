from django.contrib import admin
from .models import MessageHistory, SpeedData, Location, Trip, CurrentData, VoltageData, PowerData
from .models import Switch_EncodingData, S_Error_StatusData, RPMData, Motor_StateData, CruiseData, M_Error_StatusData, ThrottleData, BrakeData, Meter_CountData, MQTTError

#columns
class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ("id", "topic", "date", "trip")
class MQTTErrorAdmin(admin.ModelAdmin):
    list_display = ("trip", "module", "event", "time", "error")
class LocationAdmin(admin.ModelAdmin):
    list_display = ("id", "trip", "date", "latitude", "longitude")
# Register your models here.
admin.site.register(MQTTError, MQTTErrorAdmin)
admin.site.register(Switch_EncodingData)
admin.site.register(RPMData)
admin.site.register(S_Error_StatusData)
admin.site.register(Motor_StateData)
admin.site.register(CruiseData)
admin.site.register(M_Error_StatusData)
admin.site.register(ThrottleData)
admin.site.register(Meter_CountData)
admin.site.register(BrakeData)
admin.site.register(CurrentData)
admin.site.register(VoltageData)
admin.site.register(PowerData)
admin.site.register(MessageHistory, MessageHistoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Trip)
admin.site.register(SpeedData)

