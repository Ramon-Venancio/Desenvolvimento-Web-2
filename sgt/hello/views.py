from django.shortcuts import render
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse('Hello, World')

def greet(request, name):
    return HttpResponse(f"Olá, {name.capitalize()}!")

def html(request, name):
    return render(request, 'hello/greet.html', {
        'name':name.title(),
    })

def tia_zap(request, name):
    now = datetime.datetime.now()

    return render(request, 'hello/tia_zap.html', {
        'dia': now.hour < 18,
        'name': name.title(),
    })
# Create your views here.