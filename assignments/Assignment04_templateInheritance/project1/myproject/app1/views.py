from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def about(request):
    return render(request, 'all_temp1/about.html')


def contact(request):
    return render(request, 'all_temp1/contact.html')


def helpage(request):
    return render(request, 'all_temp1/helpage.html')


def home(request):
    return render(request, 'all_temp1/home.html')


def testimony(request):
    return render(request, 'all_temp1/testimony.html')
