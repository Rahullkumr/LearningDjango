from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def loginpage(request):
    if request.method == 'POST':
        username_data = request.POST['username']
        password_data = request.POST['password']
        u = authenticate(username=username_data, password=password_data)

        if u is not None:
            login(request, u)   # stored in the request variable
            messages.add_message(request, messages.SUCCESS,
                                 'Login Successfull !!!! ')
            return redirect('profile')
        else:
            messages.add_message(
                request, messages.ERROR, 'Wrong Credentials. Please try again or Register ')
            return render(request, 'loginpage.html')

    return render(request, 'loginpage.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        try:
            u = User.objects.get(username=username)
            if u:
                messages.add_message(
                    request, messages.WARNING, 'Username already exists, use different credentials')
            return render(request, 'register.html')

        except:
            u = User.objects.create(
                first_name=firstname, last_name=lastname, email=email, username=username)
            u.set_password(password)
            u.save()
            return redirect('loginpage')

    return render(request, 'register.html')


@login_required(login_url='loginpage')
def logoutme(request):
    logout(request)  # it will erase session values
    return redirect('loginpage')


@login_required(login_url='loginpage')
def profile(request):
    return render(request, 'profile.html')


@login_required(login_url='loginpage')
def updateprofile(request, pk):
    u = get_object_or_404(User, id=pk)
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']

        # overriding the db values
        u.first_name = firstname
        u.last_name = lastname
        u.email = email
        u.username = username
        u.save()
        messages.add_message(request, messages.SUCCESS,
                             'Profile Update Successfull !!!! ')
        return redirect('profile')
    return render(request, 'updateprofile.html')


@login_required(login_url='loginpage')
def changepass(request):

    if request.method == 'POST':
        np = request.POST['password']
        user = User.objects.get(username=request.user)
        user.set_password(np)
        user.save()
        return redirect('loginpage')

    return render(request, 'changepass.html')


def about(request):
    return render(request, 'about.html')
