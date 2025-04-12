from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import StudentModel
# Create your views here.


def home(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)
        print(form)  # prints source code of form along with value from the ui
        print(form.cleaned_data)  # works only if above print() is present
        # prints field name and its ui value in key:value format(i.e dictionary);

# Day 2:
        if form.is_valid():

            # THREE ways to CREATE a new student:

            # FIRST APPROACH (jabardasti har column ko create kro)
            # StudentModel.objects.create(
            #     sname = form.cleaned_data['sname'],
            #     srollno = form.cleaned_data['srollno'],
            #     course = form.cleaned_data['course']
            # )

            # SECOND APPROACH (using dictionary unpacking with ** operator)
            # StudentModel.objects.create(**form.cleaned_data)

            # THIRD APPROACH (Uses a custom create() method defined in the form class)
            form.create()
            return redirect('homepage')

    context = {
        'formkey': StudentForm(),
        'data': StudentModel.objects.all()
    }

    return render(request, 'home.html', context)


def edit(request, pk):
    stu = StudentModel.objects.get(id=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.update(stu)
            return redirect('homepage')
    form = StudentForm(
        initial={
            'sname': stu.sname,
            'srollno': stu.srollno,
            'course': stu.course,
        }
    )
    context = {'form': form}
    return render(request, 'edit.html', context)


def deletepage(request, pk):
    stu = StudentModel.objects.get(id=pk)
    stu.delete()
    return redirect('homepage')
