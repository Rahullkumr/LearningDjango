from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def views1(request):
    return HttpResponse('<h1>This is view 1/5 from app1</h1>')

def views2(request):
    return HttpResponse('<h1>This is view 2/5 from app1</h1>')

def views3(request):
    return HttpResponse('<h1>This is view 3/5 from app1</h1>')

def views4(request):
    return HttpResponse('<h1>This is view 4/5 from app1</h1>')

def views5(request):
    return HttpResponse('<h1>This is view 5/5 from app1</h1>')
