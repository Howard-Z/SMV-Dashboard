import json
from .models import MQTTError, Trip
from datetime import datetime
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class DashboardConsumer(WebsocketConsumer):
    #GROUP NAME: speed
    #TYPE NAME: data.notif
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            'speed',
            self.channel_name
        )
        self.groups.append("speed")
        self.accept()
        MQTTError.objects.create(module='ws', event='connect', message='connected', error=False, time=datetime.now(), trip=Trip.objects.last())


    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            'speed',
            self.channel_name
        )
        MQTTError.objects.create(module='ws', event='disconnect', message='disconnected', error=False, time=datetime.now(), trip=Trip.objects.last())

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))
    def data_notif(self, event):
        self.send(text_data=json.dumps({
                'type': 'data.notif',
                'module': event['module'],
                'content': event['content'],
                'error': event['error']
            })
        )

class TeamConsumer(WebsocketConsumer):
    #GROUP NAME: teamdata
    #TYPE NAME: team.notif    
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            'teamdata',
            self.channel_name
        )
        self.groups.append("teamdata")
        self.accept()
        MQTTError.objects.create(module='ws', event='connect', message='connected', error=False, time=datetime.now(), trip=Trip.objects.last())

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            'teamdata',
            self.channel_name
        )
        MQTTError.objects.create(module='ws', event='disconnect', message='disconnected', error=False, time=datetime.now(), trip=Trip.objects.last())

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))
    def team_notif(self, event):
        self.send(text_data=json.dumps({
                'type': 'team.notif',
                'module': event['module'],
                'content': event['content'],
                'error': event['error']
            })
        )