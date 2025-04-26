from django.shortcuts import render, redirect
from .models import Patient


# Create your views here.


def about(request):
    return render(request, 'about.html')


def registration(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        state = request.POST.get('state')
        aadhaar = request.POST.get('aadhaar')
        email = request.POST.get('email')
        health_problem = request.POST.get('health_problem')
        date_of_visit = request.POST.get('date_of_visit')

        Patient.objects.create(
            full_name=full_name,
            phone_number=phone_number,
            address=address,
            age=age,
            gender=gender,
            state=state,
            aadhaar=aadhaar,
            email=email,
            health_problem=health_problem,
            date_of_visit=date_of_visit
        )
        return redirect('homepage')

    return render(request, 'registration.html')
