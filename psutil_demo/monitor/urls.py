from django.urls import path
from . import log_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),    # 首页
    path('cpu/', views.cpu_m, name='cpu'),  # cpu
    path('mem/', views.mem_m, name='mem'),  # mem
    path('net/', views.net_m, name='net'),  # net
    path('cpu_log/', log_views.cpu_avg_log, name='cpulog'),  # cpu log
    path('liquid/', views.liquid, name='liquid'),  # test liquid
]
