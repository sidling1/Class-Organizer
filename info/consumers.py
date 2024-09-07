import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from info.models import *

class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        # Change this
        self.room_name = f"room_{self.scope['url_route']['kwargs']['course_id']}"
        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_name, self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json
        # print('Recieved',message)

        event = {
            'type':'send_message',
            'message': message
        }

        await self.channel_layer.group_send(self.room_name, event)

    async def send_message(self, event):
        data = event['message']
        await self.create_message(data=data)
        
        sender = await self.get_student_name(data['sender_id'])
        
        response_data = {
            'sender': sender,
            'message': data['message'],
            'sender_id': data['sender_id']
        }


        print('sending message')

        await self.send(text_data=json.dumps({'message': response_data}))

    @database_sync_to_async
    def get_student_name(self, id):
        return Student.objects.get(USN = id).name
    
    @database_sync_to_async
    def create_message(self, data):
        # get_room_by_name = Room.objects.get(room_name=data['room_name'])
        msg = data['message']
        course_id = data['course_id']
        sender_id = data['sender_id']

        course = Course.objects.get(id=course_id)
        grp = ChatGroup.objects.get(course=course)
        sender = Student.objects.get(USN=sender_id).user

        print("Saving Message to DB")

        ChatMessage.objects.create(group=grp, sender=sender, message=msg)
        # new_message.save()