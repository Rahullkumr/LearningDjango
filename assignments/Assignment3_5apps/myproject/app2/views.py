from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def fun1(request):
    return HttpResponse('This is function 1/5 from app2')


def fun2(request):
    return HttpResponse('This is function 2/5 from app2')


def fun3(request):
    return HttpResponse('This is function 3/5 from app2')


def fun4(request):
    return HttpResponse('This is function 4/5 from app2')


def fun5(request):
    return HttpResponse('This is function 5/5 from app2')
