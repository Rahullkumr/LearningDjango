from django.shortcuts import render

# Create your views here.


def car(request):
    return render(request, 'all_temp10/car.html')


def bike(request):
    return render(request, 'all_temp10/bike.html')


def bicycle(request):
    return render(request, 'all_temp10/bicycle.html')


def rickshaw(request):
    return render(request, 'all_temp10/rickshaw.html')


def truck(request):
    return render(request, 'all_temp10/truck.html')
