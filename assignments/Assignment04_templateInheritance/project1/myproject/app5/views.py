from django.shortcuts import render

# Create your views here.


def submarine(request):
    return render(request, 'all_temp5/submarine.html')


def missile(request):
    return render(request, 'all_temp5/missile.html')


def fighterjet(request):
    return render(request, 'all_temp5/fighterjet.html')


def helicopter(request):
    return render(request, 'all_temp5/helicopter.html')


def rocket(request):
    return render(request, 'all_temp5/rocket.html')
