import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class SpeedConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)(
            'speed',
            self.channel_name
        )
        self.groups.append("speed")
        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            'speed',
            self.channel_name
        )
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))
    def data_notif(self, event):
        self.send(text_data=json.dumps({
                'type': 'data.notif',
                'module': event['module'],
                'content': event['content']
            })
        )
    def battery_notif(self, event):
        self.send(text_data=json.dumps({
                'type': 'battery.notif',
                'content': event['content']
            })
        )