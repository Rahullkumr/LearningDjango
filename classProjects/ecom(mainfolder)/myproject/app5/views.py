from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def aeroplane(request):
    # return HttpResponse('This is views1 from app5')
    return render(request, 'all_temp5/aeroplane.html')


def train(request):
    # return HttpResponse('This is views2 from app5')
    return render(request, 'all_temp5/train.html')


def ship(request):
    # return HttpResponse('This is views3 from app5')
    return render(request, 'all_temp5/ship.html')
