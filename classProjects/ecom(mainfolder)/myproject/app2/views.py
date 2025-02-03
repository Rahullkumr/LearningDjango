from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def mobile(request):
    return HttpResponse('This page is about mobiles')


def charger(request):
    return HttpResponse('This page is about chargers')


def headphone(request):
    return HttpResponse('This page is about headphone')


def cable(request):
    return HttpResponse('This page is about cable')


def earphone(request):
    return HttpResponse('This page is about earphone')
