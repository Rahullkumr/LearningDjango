from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def login_(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        u=authenticate(username=username,password=password)
        if u:
            login(request,u)
            return redirect('home')

    return render(request,'login_.html',{'login_nav':True})


def register(request):

    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        print(firstname,lastname,email,username,password)
        u=User.objects.create(
            first_name=firstname,
            last_name=lastname,
            email=email,
            username=username
        )
        u.set_password(password)
        u.save()
        return redirect('login_')


    return render(request,'register.html',{'login_nav':True})

@login_required(login_url='login_')
def logout_(request):
    logout(request)
    return redirect('login_')

@login_required(login_url='login_')
def profile(request):



    return render(request,'profile.html',{'profile_nav':True})

@login_required(login_url='login_')
def changepass(request):
    if request.method == 'POST':
        password=request.POST['password']
        u=User.objects.get(username=request.user)
        u.set_password(password)
        u.save()
        return redirect('login_')
    return render(request,'changepass.html')
