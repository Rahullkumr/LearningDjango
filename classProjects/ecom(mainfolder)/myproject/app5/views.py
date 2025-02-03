from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def views1(request):
    return HttpResponse('This is views1 from app5')


def views2(request):
    return HttpResponse('This is views2 from app5')


def views3(request):
    return HttpResponse('This is views3 from app5')


def views4(request):
    return HttpResponse('This is views4 from app5')


def views5(request):
    return HttpResponse('This is views5 from app5')
