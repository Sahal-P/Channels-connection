import os
from django.core.asgi import get_asgi_application
from django.conf import settings
from uvicorn import run
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "channels.settings")

application = get_asgi_application()

if __name__ == "__main__":
    run(
        application,
        host=settings.ALLOWED_HOSTS[0],
        port=settings.PORT,
        debug=settings.DEBUG,
        log_level="info",
    )
    
ws_patters = [
    path('test/',)
]

application = ProtocolTypeRouter({
    'websocket' : URLRouter(ws_patters)
})