from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello, World')

def greet(request, name):
    return HttpResponse(f"Olá, {name.capitalize()}!")

def html(request, name):
    return render(request, 'hello/index.html', {
        'name':name.capitalize()
    })
# Create your views here.