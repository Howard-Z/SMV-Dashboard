from .models import *
#SET TOPICS HERE: FORMAT: (mqtt_topic, device.data, model)
topics_list = {
    #bear_1
    "/Bear_1/RPM": {
        "name": "bear1.rpm",
        "model": RPMData
        #chart
    },
        "/Bear_1/Motor_State": {
        "name": "bear1.motor_state",
        "model": Motor_StateData
        #io
    },
        "/Bear_1/Cruise": {
        "name": "bear1.cruise",
        "model": CruiseData
        #ignore
    },
        "/Bear_1/M_Error_Status": {
        "name": "bear1.m_error_status",
        "model": M_Error_StatusData
        #error 1, check, io
    },
        "/Bear_1/Throttle": {
        "name": "bear1.throttle",
        "model": ThrottleData,
        "max": 100,
        "min": 0
        #error above 1028: check teensy output range, ignore
    },
    "/Bear_1/Brake": {
        "name": "bear1.brake",
        "model": BrakeData
        #check back, ignore
    },
    "/Bear_1/Meter_Count": {
        "name": "bear1.meter_count",
        "model": Meter_CountData
        #ignore
    },    
#bear_2
    "/Bear_2/RPM": {
        "name": "bear2.rpm",
        "model": RPMData
    },
    "/Bear_2/Motor_State": {
        "name": "bear2.motor_state",
        "model": Motor_StateData
    },

    "/Bear_2/Cruise": {
        "name": "bear2.cruise",
        "model": CruiseData
    },
    "/Bear_2/M_Error_Status": {
        "name": "bear2.m_error_status",
        "model": M_Error_StatusData
        #error 1, check

    },

    "/Bear_2/Throttle": {
        "name": "bear2.throttle",
        "model": ThrottleData
    },
    "/Bear_2/Brake": {
        "name": "bear2.brake",
        "model": BrakeData
    },
    "/Bear_2/Meter_Count": {
        "name": "bear2.meter_count",
        "model": Meter_CountData
    },
    #power_control
    "/Power_Control/Current": {
        "name": "power_control.current",
        "model": CurrentData
        # >120 A check back
    },
    "/Power_Control/Voltage": {
        "name": "power_control.voltage",
        "model": VoltageData
        # >55 V
    },
    "/Power_Control/Power": {
        "name": "power_control.power",
        "model": PowerData
    },
    "/Power_Control/Energy": {
        "name": "power_control.energy",
        "model": EnergyData
    },
    "/Power_Control/T1": {
        "name": "power_control.t1",
        "model": T1Data
    },
    "/Power_Control/T2": {
        "name": "power_control.t2",
        "model": T2Data
    },
    "/Power_Control/T3": {
        "name": "power_control.t3",
        "model": T3Data
    },
    "/Power_Control/P_Error_Status": {
        "name": "power_control.p_error_status",
        "model": P_Error_StatusData
    },
    #Steering
    "/Steering_Wheel/Switch_Encoding": {
        "name": "steering_wheel.switch_encoding",
        "model": Switch_EncodingData
        #ignore
    },
    "/Steering_Wheel/S_Error_Status": {
        "name": "steering_wheel.s_error_status",
        "model": S_Error_StatusData
        #io
    },
    #DAQMessage
    "/DAQ/Speed": {
        "name": "daq.speed",
        "model": SpeedData,
    },
    "/DAQ/Longitude": {
        "name": "daq.longitude",
        "model": Location
    },
    "/DAQ/Latitude": {
        "name": "daq.latitude",
        "model": Location
    }
}