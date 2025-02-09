from django.shortcuts import render

# Create your views here.


def about(request):
    return render(request, 'all_temp8/about.html')


def contact(request):
    return render(request, 'all_temp8/contact.html')


def helpage(request):
    return render(request, 'all_temp8/helpage.html')


def home(request):
    return render(request, 'all_temp8/home.html')


def testimony(request):
    return render(request, 'all_temp8/testimony.html')
