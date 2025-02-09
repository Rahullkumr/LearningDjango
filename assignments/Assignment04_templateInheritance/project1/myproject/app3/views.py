from django.shortcuts import render

# Create your views here.


def shirt(request):
    return render(request, 'all_temp3/shirt.html')


def pant(request):
    return render(request, 'all_temp3/pant.html')


def shoe(request):
    return render(request, 'all_temp3/shoe.html')


def coat(request):
    return render(request, 'all_temp3/coat.html')


def sweater(request):
    return render(request, 'all_temp3/sweater.html')
