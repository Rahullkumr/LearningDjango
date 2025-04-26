from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def loginpage(request):
    return render(request, 'loginpage.html')


def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        User.objects.create(first_name=name, email=email,
                            username=username, password=password)
        messages.success(request, "Signing up successful !!!")

    return render(request, 'signup.html')


def profile(request):
    return render(request, 'profile.html')


def update_profile(request):
    return render(request, 'update_profile.html')


def changepass(request):
    return render(request, 'changepass.html')


def logout(request):
    ...
