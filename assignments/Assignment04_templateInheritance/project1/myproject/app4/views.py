from django.shortcuts import render

# Create your views here.


def car(request):
    return render(request, 'all_temp4/car.html')


def bike(request):
    return render(request, 'all_temp4/bike.html')


def bicycle(request):
    return render(request, 'all_temp4/bicycle.html')


def rickshaw(request):
    return render(request, 'all_temp4/rickshaw.html')


def truck(request):
    return render(request, 'all_temp4/truck.html')
