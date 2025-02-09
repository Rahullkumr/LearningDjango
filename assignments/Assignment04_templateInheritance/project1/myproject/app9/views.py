from django.shortcuts import render

# Create your views here.


def submarine(request):
    return render(request, 'all_temp9/submarine.html')


def missile(request):
    return render(request, 'all_temp9/missile.html')


def fighterjet(request):
    return render(request, 'all_temp9/fighterjet.html')


def helicopter(request):
    return render(request, 'all_temp9/helicopter.html')


def rocket(request):
    return render(request, 'all_temp9/rocket.html')
