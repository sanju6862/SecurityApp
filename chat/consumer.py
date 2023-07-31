# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user1_id = self.scope['url_route']['kwargs']['id1']
        self.user2_id = self.scope['url_route']['kwargs']['id2']

        # Code to handle user authentication, authorization, and room validation
        # For example, you can check if the users are allowed to chat, if they exist, etc.

        self.room_group_name = f'chat_{self.user1_id}_{self.user2_id}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        # Save the message to the database or perform any additional processing here

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))
