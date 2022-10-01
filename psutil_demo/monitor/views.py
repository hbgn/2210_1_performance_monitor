from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'index.html')


def cpu_m(request):
    return render(request, 'cpu_m.html')
