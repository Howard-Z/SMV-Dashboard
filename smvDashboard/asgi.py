import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "smvDashboard.settings") #DO NOT MOVE. NEED TO SET THIS ENVVAR FIRST

# Initialize Django ASGI application early to ensure the AppRegistry
# is populated before importing code that may import ORM models.
from django.core.asgi import get_asgi_application
django_asgi_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

from mqtt.routing import application



import mqtt.routing

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(application))
        ),
    }
)