from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def chat(request):
    return render(request, 'chat.html')
