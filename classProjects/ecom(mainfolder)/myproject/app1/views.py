from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    print('hello world')
    return HttpResponse('homepage')


def about(request):
    return HttpResponse('about page')
