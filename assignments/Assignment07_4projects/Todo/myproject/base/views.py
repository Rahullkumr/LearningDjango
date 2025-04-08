from django.shortcuts import render, redirect, get_object_or_404
from base.models import Tasks

# Create your views here.


def alltasks(request):
    all_tasks = Tasks.objects.all()
    return render(request, 'alltasks.html', {'all_tasks': all_tasks})


def addtask(request):
    if request.method == 'POST':
        task_fromui = request.POST['task_fromui']
        Tasks.objects.create(task_todo=task_fromui)
        return redirect('alltasks')
    return render(request, 'addtask.html')


def edit(request, pk):
    task_from_db = get_object_or_404(Tasks, id=pk)
    if request.method == 'POST':
        task_fromui = request.POST.get('task_fromui')
        if task_fromui:
            task_from_db.task_todo = task_fromui
            task_from_db.save()
        return redirect('alltasks')
    return render(request, 'edit.html', {'data': task_from_db})


def delete(request, pk):
    if pk:
        task_to_be_deleted = get_object_or_404(Tasks, id=pk)
        task_to_be_deleted.delete()
        return redirect('alltasks')
    return render(request, 'alltasks.html')
