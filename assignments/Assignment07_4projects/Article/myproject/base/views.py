from django.shortcuts import render
from base.models import Article

# Create your views here.

data_from_db = Article.objects.all()


def home(request):
    context = {
        'indian_data': data_from_db
    }
    return render(request, 'home.html', context)


def events(request):
    return render(request, 'events.html')


def news(request):
    return render(request, 'news.html')


def about(request):
    return render(request, 'about.html')


def read(request, recieved_button_ka_id):

    for i in data_from_db:
        if i.id == recieved_button_ka_id:
            context = {'primary_key': i}

    return render(request, 'read.html', context)
