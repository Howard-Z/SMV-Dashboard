import json
from .models import MQTTError, Trip, Location
from datetime import datetime
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .helper import send_location


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
        print("CLOSING")
        print(close_code)
        MQTTError.objects.create(module='ws', event='disconnect', message=f'disconnected with {close_code}', error=False, time=datetime.now(), trip=Trip.objects.last())

    def receive(self, text_data):
        date = datetime.fromtimestamp(float(text_data)/1000.0)
        Trip.objects.last().active=False
        Trip.objects.create(start=date, date_created=date, active=True,name=f"{date} trip (auto)")

    def data_notif(self, event):
        print(event)
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
        self.send(text_data=json.dumps({
            'type': 'team.notif',
            'module': "timing",
            'content': f"{Trip.objects.last().start}",
            'error': False
            })
        )
        MQTTError.objects.create(module='ws', event='connect', message='connected', error=False, time=datetime.now(), trip=Trip.objects.last())

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            'teamdata',
            self.channel_name
        )
        MQTTError.objects.create(module='ws', event='disconnect', message='disconnected', error=False, time=datetime.now(), trip=Trip.objects.last())

    def receive(self, text_data):
        print(text_data)

    def team_notif(self, event):
        print(event)
        self.send(text_data=json.dumps({
                'type': 'team.notif',
                'module': event['module'],
                'content': event['content'],
                'error': event['error']
            })
        )