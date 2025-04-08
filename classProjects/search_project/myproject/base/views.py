from django.shortcuts import render
from .models import Fruits
from django.db.models import Q
'''
what?
    Q is a class from django.db.models that helps to create complex queries using AND, OR or NOT conditions

Why should you use Q()?
    - To create more complex filters using AND, OR or NOT conditions 
    - for dynamic queries based on user input
'''


def homepage(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_fruits = Fruits.objects.filter(
            Q(name__icontains=q) | Q(desc__icontains=q))
        # | it is OR logic
    else:
        all_fruits = Fruits.objects.all()

    return render(request, 'homepage.html', {'all_fruits': all_fruits})
