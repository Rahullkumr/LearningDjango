from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def red(request):
    return HttpResponse('<h1>Red page</h1>')


def green(request):
    return HttpResponse('<h1>green page</h1>')


def blue(request):
    return HttpResponse('<h1>blue page</h1>')


def yellow(request):
    return HttpResponse('<h1>yellow page</h1>')


def violet(request):
    return HttpResponse('<h1>violet page</h1>')


def magenta(request):
    return HttpResponse('<h1>magenta page</h1>')


def chocolate(request):
    return HttpResponse('<h1>chocolate page</h1>')


def black(request):
    return HttpResponse('<h1>black page</h1>')


def white(request):
    return HttpResponse('<h1>white page</h1>')


def gray(request):
    return HttpResponse('<h1>gray page</h1>')
