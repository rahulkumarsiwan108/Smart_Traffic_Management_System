import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TrafficConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.send(text_data=json.dumps({"message": "WebSocket Connected"}))

    async def disconnect(self, close_code):
        print(f"WebSocket Disconnected: {close_code}")

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.send(text_data=json.dumps({"response": f"Received: {data}"}))
