from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import StudentModel
# Create your views here.


def home(request):
    # read
    data = StudentModel.objects.all()

    # create
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    return render(request, 'home.html', {'form': StudentForm(), 'data': data})


def edit(request, pk):
    stu = StudentModel.objects.get(id=pk)
    form = StudentForm(instance=stu)

    # update
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=stu)
        if form.is_valid():
            form.save()
            return redirect('homepage')

    return render(request, 'edit.html', {'form': form})


# delete
def deletepage(request, pk):
    stu = StudentModel.objects.get(id=pk)
    stu.delete()
    return redirect('homepage')
