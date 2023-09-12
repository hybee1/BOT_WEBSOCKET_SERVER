
import json

from channels.generic.websocket import AsyncWebsocketConsumer


class bot_server_websocket(AsyncWebsocketConsumer):


    async def connect(self):
        await self.accept()

