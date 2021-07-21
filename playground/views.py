from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(req): 
    return HttpResponse('Hello world!')


def say_goodbye(req): 
    x = 1
    y = 2
    return HttpResponse('Goodbye')