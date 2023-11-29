from django.contrib import admin
from .models import MessageHistory, SpeedData, Location, Trip, CurrentData, VoltageData, PowerData
from .models import EnergyData, T1Data, T2Data, T3Data, Switch_EncodingData, S_Error_StatusData, RPMData, Motor_StateData, CruiseData, M_Error_StatusData, ThrottleData, BrakeData, Meter_CountData, MQTTError, P_Error_StatusData

#columns
class MessageHistoryAdmin(admin.ModelAdmin):
    list_display = ("id", "topic", "date", "trip")

# Register your models here.
admin.site.register(MQTTError)
admin.site.register(EnergyData)
admin.site.register(T1Data)
admin.site.register(T2Data)
admin.site.register(T3Data)
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
admin.site.register(P_Error_StatusData)
admin.site.register(MessageHistory, MessageHistoryAdmin)
admin.site.register(Location)
admin.site.register(Trip)
admin.site.register(SpeedData)

