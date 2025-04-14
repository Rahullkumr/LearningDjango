from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from base.models import Article

# Create your views here.

data_from_db = Article.objects.all()


@login_required(login_url='loginpage')
def home(request):
    context = {'indian_data': data_from_db}
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


@login_required(login_url='loginpage')
def read(request, recieved_button_ka_id):

    for i in data_from_db:
        if i.id == recieved_button_ka_id:
            context = {'primary_key': i}

    return render(request, 'read.html', context)


@login_required(login_url='loginpage')
def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_articles = Article.objects.filter(Q(title__icontains=q))
    else:
        all_articles = None
    return render(request, 'search.html', {'all_articles': all_articles})
