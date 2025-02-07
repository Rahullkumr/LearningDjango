from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def red(request):
    # return HttpResponse('<h1>This is red from app3</h1>')
    return render(request, 'red.html')


def green(request):
    # return HttpResponse('<h1>This is green from app3</h1>')
    return render(request, 'green.html')


def blue(request):
    # return HttpResponse('<h1>This is blue from app3</h1>')
    return render(request, 'blue.html')
