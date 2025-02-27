from django.shortcuts import render

# Create your views here.

stu_data = [
    {
        'roll': 1,
        'name': 'Rahul Kumar',
        'email': 'rahul@gmail.com',
        'subject': 'Python',
        'city': 'Ranchi',
    },
    {
        'roll': 2,
        'name': 'Avinash',
        'email': 'avi@gmail.com',
        'subject': 'Django',
        'city': 'Pune',
    },
    {
        'roll': 3,
        'name': 'Manish Kumar',
        'email': 'man@gmail.com',
        'subject': 'Html',
        'city': 'Chennai',
    },
    {
        'roll': 4,
        'name': 'Sontake Ajay',
        'email': 'aj@gmail.com',
        'subject': 'Css',
        'city': 'Nagpur',
    },
]


def homepage(request):
    return render(request, 'homepage.html')


def reg_form(request):
    return render(request, 'reg_form.html')


def stu_list(request):
    context = {'stu_list_nav': True, 'students': stu_data}
    return render(request, 'stu_list.html', context)


def details(request, primary_key):
    for student in stu_data:
        if student['roll'] == primary_key:
            context = {'stu_details': student}
    return render(request, 'details.html', context)
