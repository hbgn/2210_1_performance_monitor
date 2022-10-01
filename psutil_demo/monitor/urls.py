from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # 首页
    path('cpu/', views.cpu_m, name='cpu'), # cpu页
]
