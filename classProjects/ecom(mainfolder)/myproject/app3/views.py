from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'all_temp3/app3_homepage.html')


def red(request):
    # return HttpResponse('<h1>This is red from app3</h1>')

    a = 'red'
    context = {'red_data': a}
    return render(request, 'all_temp3/red.html', context=context)


def green(request):
    # return HttpResponse('<h1>This is green from app3</h1>')

    a = 'green'
    context = {'green_data': a}
    return render(request, 'all_temp3/green.html', context=context)


def blue(request):
    # return HttpResponse('<h1>This is blue from app3</h1>')

    a = 'blue'
    context = {'blue_data': a}
    return render(request, 'all_temp3/blue.html', context=context)
