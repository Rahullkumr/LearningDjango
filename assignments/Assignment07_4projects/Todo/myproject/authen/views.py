from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def loginpage(request):
    if request.method == 'POST':
        username_data = request.POST['username']
        password_data = request.POST['password']
        u = authenticate(username=username_data, password=password_data)

        if u is not None:
            login(request, u)   # stored in the request variable
            return redirect('alltasks')
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


def logoutme(request):
    logout(request)  # it will erase session values
    return redirect('loginpage')
