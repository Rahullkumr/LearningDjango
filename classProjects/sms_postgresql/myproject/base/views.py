from django.shortcuts import render, redirect, get_object_or_404
from .models import StudentModel
# Create your views here.


def students(request):
    if request.method == 'POST':
        name = request.POST['name']
        rollno = request.POST['rollno']
        course = request.POST['course']
        StudentModel.objects.create(
            name=name,
            rollno=rollno,
            course=course
        )
    all_data = StudentModel.objects.all()
    return render(request, 'students.html', {'all_data': all_data})


def student(request, pk):
    student_data = get_object_or_404(StudentModel, id=pk)
    if request.method == 'POST':
        name = request.POST['name']
        rollno = request.POST['rollno']
        course = request.POST['course']

        student_data.name = name
        student_data.rollno = rollno
        student_data.course = course
        student_data.save()
        return redirect('students')

    return render(request, 'student.html', {'student': student_data})


def deleteme(request, pk):
    if pk:
        student_to_be_deleted = get_object_or_404(StudentModel, id=pk)
        student_to_be_deleted.delete()
        return redirect('students')
    return render(request, 'students.html')
