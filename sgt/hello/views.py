from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello, World')

def greet(request, name):
    return HttpResponse(f"Hello, {name}!")

# Create your views here.