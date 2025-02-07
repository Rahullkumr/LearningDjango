from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    # print('hello world')
    # return HttpResponse('homepage')

    # today learnt about templates, so we will use below code
    return render(request, 'home.html')


def about(request):
    # return HttpResponse('about page')

    return render(request, 'about.html')
