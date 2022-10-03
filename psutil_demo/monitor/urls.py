from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    # 首页
    path('cpu/', views.cpu_m, name='cpu'),  # cpu页
    path('mem/', views.mem_m, name='mem'),  # mem页
    path('net/', views.net_m, name='net'),  # net页
    path('liquid/', views.liquid, name='liquid'),  # test liquid
]
