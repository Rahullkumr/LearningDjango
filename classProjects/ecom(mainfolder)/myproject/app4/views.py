from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Sachin(request):
    # return HttpResponse('This is Sachin from app4')
    return render(request, 'sachin.html')


def Dhoni(request):
    # return HttpResponse('This is Dhoni from app4')
    return render(request, 'dhoni.html')


def Virat(request):
    # return HttpResponse('This is Virat from app4')
    return render(request, 'virat.html')
