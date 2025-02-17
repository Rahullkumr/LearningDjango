from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'all_temp/home.html')


def about(request):
    return render(request, 'all_temp/about.html')


def products(request):
    return render(request, 'all_temp/products.html')
