from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from base.models import Tasks
from django.contrib.auth.models import User


# Create your views here.


@login_required(login_url='loginpage')
def alltasks(request):
    all_tasks = Tasks.objects.all()
    return render(request, 'alltasks.html', {'all_tasks': all_tasks})


@login_required(login_url='loginpage')
def addtask(request):
    if request.method == 'POST':
        task_fromui = request.POST['task_fromui']
        Tasks.objects.create(task_todo=task_fromui)
        return redirect('alltasks')
    return render(request, 'addtask.html')


@login_required(login_url='loginpage')
def edit(request, pk):
    task_from_db = get_object_or_404(Tasks, id=pk)
    if request.method == 'POST':
        task_fromui = request.POST.get('task_fromui')
        if task_fromui:
            task_from_db.task_todo = task_fromui
            task_from_db.save()
        return redirect('alltasks')
    return render(request, 'edit.html', {'data': task_from_db})


@login_required(login_url='loginpage')
def delete(request, pk):
    if pk:
        task_to_be_deleted = get_object_or_404(Tasks, id=pk)
        task_to_be_deleted.delete()
        return redirect('alltasks')
    return render(request, 'alltasks.html')


@login_required(login_url='loginpage')
def searchtask(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_tasks = Tasks.objects.filter(Q(task_todo__icontains=q))
    else:
        all_tasks = None
    return render(request, 'searchtask.html', {'all_tasks': all_tasks})


@login_required(login_url='loginpage')
def profile(request):
    return render(request, 'profile.html')


@login_required(login_url='loginpage')
def changepass(request):

    if request.method == 'POST':
        np = request.POST['password']
        user = User.objects.get(username=request.user)
        user.set_password(np)
        user.save()
        return redirect('loginpage')

    return render(request, 'changepass.html')


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
