from django.shortcuts import render

# Create your views here.


def electro_home(request):
    return render(request, 'electro_html/electro_home.html')


def electro_about(request):
    return render(request, 'electro_html/electro_about.html')


def electro_cart(request):
    return render(request, 'electro_html/electro_cart.html')


def laptop(request):
    return render(request, 'electro_html/laptop.html')


def mobile(request):
    return render(request, 'electro_html/mobile.html')


def tv(request):
    return render(request, 'electro_html/tv.html')
