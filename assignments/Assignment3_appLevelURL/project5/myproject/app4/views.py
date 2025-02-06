from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def AndhraPradesh(request):
    return HttpResponse('<h1>AndhraPradesh page</h1>')


def Bihar(request):
    return HttpResponse('<h1>Bihar page</h1>')


def Chandigarh(request):
    return HttpResponse('<h1>Chandigarh page</h1>')


def Delhi(request):
    return HttpResponse('<h1>Delhi page</h1>')


def Haryana(request):
    return HttpResponse('<h1>Haryana page</h1>')


def Jharkhand(request):
    return HttpResponse('<h1>Jharkhand page</h1>')


def Maharashtra(request):
    return HttpResponse('<h1>Maharashtra page</h1>')


def Orissa(request):
    return HttpResponse('<h1>Orissa page</h1>')


def Telangana(request):
    return HttpResponse('<h1>Telangana page</h1>')


def Mizoram(request):
    return HttpResponse('<h1>Mizoram page</h1>')
