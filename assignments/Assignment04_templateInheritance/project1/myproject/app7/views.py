from django.shortcuts import render

# Create your views here.


def shirt(request):
    return render(request, 'all_temp7/shirt.html')


def pant(request):
    return render(request, 'all_temp7/pant.html')


def shoe(request):
    return render(request, 'all_temp7/shoe.html')


def coat(request):
    return render(request, 'all_temp7/coat.html')


def sweater(request):
    return render(request, 'all_temp7/sweater.html')
