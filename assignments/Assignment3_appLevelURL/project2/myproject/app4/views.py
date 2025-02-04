from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    return HttpResponse('<h1>Homepage</h1>')


def about(request):
    return HttpResponse('<h1>About</h1>')


def contact(request):
    return HttpResponse('<h1>Contact</h1>')


def help(request):
    return HttpResponse('<h1>Help</h1>')


def product(request):
    return HttpResponse('<h1>Products</h1>')
