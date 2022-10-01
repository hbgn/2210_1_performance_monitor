"""
ASGI config for websocket_chat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from . import routings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket_chat.settings')

# application = get_asgi_application() # http协议
application = ProtocolTypeRouter({
    'http': get_asgi_application(),  # 如果是http请求走这条
    'websocket': URLRouter(routings.websocket_urlpatterns) # 如果是ws请求走这条
})
