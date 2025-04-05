from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def logoutpage(request):
    logout(request)  # it will erase session values
    return redirect('loginauth')


def loginauth(request):
    if request.method == 'POST':
        username_data = request.POST['username']
        password_data = request.POST['password']
        print(username_data, password_data)

        # commented because authenticate() does not verify string format pwd, so we need something different logic
        u = authenticate(username=username_data, password=password_data)
        print(u)
        if u is not None:
            login(request, u)   # stored in the request variable
            return redirect('homepage')
        else:
            wc = True
            return render(request, 'loginauth.html', {'wc': wc})

        # try:
        #     user = User.objects.get(username=username_data)
        #     if user.password == password_data:
        #         login(request, user)
        #         return redirect('homepage')
        #     else:
        #         wcp = True
        #         return render(request, 'loginauth.html', {'wcp': wcp})
        # except:
        #     wc = True
        #     return render(request, 'loginauth.html', {'wc': wc})

    return render(request, 'loginauth.html')


def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']

        try:
            # fetch username from database and store it in u
            u = User.objects.get(username=username)
            return render(request, 'registerme.html', {'u': u})

        except:
            print(firstname, lastname, email, username, password)
            u = User.objects.create(first_name=firstname, last_name=lastname,
                                    email=email, username=username)
            # comment below two lines to store pwd in string format
            u.set_password(password)
            u.save()
            return redirect('loginauth')

    return render(request, 'registerme.html')


@login_required(login_url='loginpage')
def profile(request):
    return render(request, 'profile.html')


def changepass(request):

    if request.method == 'POST':
        np = request.POST['password']
        user = User.objects.get(username=request.user)
        user.set_password(np)
        user.save()
        return redirect('loginauth')

    return render(request, 'changepass.html')
