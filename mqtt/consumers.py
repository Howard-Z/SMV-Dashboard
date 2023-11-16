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
    def speed_notif(self, event):
        print(event)
        self.send(text_data=json.dumps({
                'type': 'speed.notif',
                'content': event['content']
            })
        )