from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'temp_base/home.html')


def about(request):
    return render(request, 'temp_base/about.html')
