from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def homepage(request):
    return HttpResponse('<h1>This is homepage</h1>')


def about(request):
    return HttpResponse('<h1>This is about</h1>')


def product(request):
    return HttpResponse('<h1>This is product</h1>')


def helppage(request):
    return HttpResponse('<h1>This is help page</h1>')


def contact(request):
    return HttpResponse('<h1>This is contact</h1>')


def category(request):
    return HttpResponse('<h1>This is category page</h1>')


def checkout(request):
    return HttpResponse('<h1>This is checkout page</h1>')


def payment(request):
    return HttpResponse('<h1>This is payment page</h1>')


def comparision(request):
    return HttpResponse('<h1>This is comparison page</h1>')


def recommendation(request):
    return HttpResponse('<h1>This is recommendation page</h1>')
