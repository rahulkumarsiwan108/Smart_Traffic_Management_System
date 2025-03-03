from django.urls import re_path
from .consumers import TrafficConsumer  # ✅ Ensure TrafficConsumer exists in consumers.py

websocket_urlpatterns = [
    re_path(r"ws/traffic/$", TrafficConsumer.as_asgi()),  # ✅ This should match WebSocket requests
]
