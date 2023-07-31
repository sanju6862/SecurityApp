# routing.py

from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/chat/<int:id1>/<int:id2>/', ChatConsumer.as_asgi()),
]
