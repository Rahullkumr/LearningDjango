from django.shortcuts import render

# Create your views here.


def blue(request):
    return render(request, 'all_temp6/blue.html')


def green(request):
    return render(request, 'all_temp6/green.html')


def red(request):
    return render(request, 'all_temp6/red.html')


def white(request):
    return render(request, 'all_temp6/white.html')


def yellow(request):
    return render(request, 'all_temp6/yellow.html')
