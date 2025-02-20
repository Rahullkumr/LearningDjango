from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse('This page is about mobiles')
    return render(request, 'all_temp2/app2_home.html')


def rectangle(request):
    # return HttpResponse('This page is about mobiles')
    context = {
        'rect_data': 'Rectangle view'
    }
    return render(request, 'all_temp2/rectangle.html', context)


def circle(request):
    # return HttpResponse('This page is about chargers')
    context = {
        'circle_data': 'Circle view'
    }
    return render(request, 'all_temp2/circle.html', context)


def square(request):
    # return HttpResponse('This page is about headphone')
    context = {
        'square_data': 'Square view'
    }
    return render(request, 'all_temp2/square.html', context)
