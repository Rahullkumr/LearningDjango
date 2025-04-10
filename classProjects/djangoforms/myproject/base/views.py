from django.shortcuts import render
from .forms import StudentForm
# Create your views here.


def home(request):

    if request.method == 'POST':
        form = StudentForm(request.POST)
        print(form)  # prints source code of form along with value from the ui
        print(form.cleaned_data)  # works only if above print() is present
        # prints field name and its ui value in key:value format(i.e dictionary);

    context = {'formkey': StudentForm()}
    return render(request, 'home.html', context)
