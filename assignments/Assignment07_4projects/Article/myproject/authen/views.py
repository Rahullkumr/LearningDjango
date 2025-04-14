from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def loginpage(request):
    if request.method == 'POST':
        username_data = request.POST['username']
        password_data = request.POST['password']
        u = authenticate(username=username_data, password=password_data)

        if u is not None:
            login(request, u)   # stored in the request variable
            return redirect('homepage')
        else:
            wc = True
            return render(request, 'loginpage.html', {'wc': wc})

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
            return render(request, 'register.html', {'u': u})

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
