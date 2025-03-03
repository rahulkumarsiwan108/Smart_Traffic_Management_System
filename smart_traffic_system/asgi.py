import os
import django
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from traffic_monitoring.routing import websocket_urlpatterns  # ✅ Ensure this import is correct

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_traffic_system.settings')
django.setup()

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # ✅ Handles HTTP requests
    "websocket": AuthMiddlewareStack(  # ✅ Adds authentication support for WebSockets
        URLRouter(websocket_urlpatterns)
    ),
})
