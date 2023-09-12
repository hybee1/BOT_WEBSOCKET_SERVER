from django.urls import path

from . import consumers

websocket_urlpatterns = [
    # path('bot_server', consumers3.bot_server_websocket.as_asgi()),
    path('bot_server', consumers.ChatConsumer.as_asgi()),
]