from django.shortcuts import render

# Create your views here.


def electro_home(request):
    return render(request, 'electro_home.html')
