from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def mobile(request):
    # return HttpResponse('This page is about mobiles')
    return render(request, 'mobile.html')


def charger(request):
    # return HttpResponse('This page is about chargers')
    return render(request, 'charger.html')


def headphone(request):
    # return HttpResponse('This page is about headphone')
    return render(request, 'headphone.html')
