from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    return HttpResponse('<h1>This is homepage</h1>')


def about(request):
    return HttpResponse('<h1>This is about</h1>')


def product(request):
    return HttpResponse('<h1>This is product</h1>')


def help(request):
    return HttpResponse('<h1>This is help</h1>')


def contact(request):
    return HttpResponse('<h1>This is contact</h1>')
