# 配置websocket 路由
from django.urls import re_path
from chat.chat_consumer import ChatConsumer
from monitor.m_consumers import Monitor_Consum

websocket_urlpatterns = [
    re_path(r'ws/(?P<websocket>\w+)/$', ChatConsumer.as_asgi()),
    re_path(r'monitor/(?P<monitor>\w+)/$', Monitor_Consum.as_asgi())
]
