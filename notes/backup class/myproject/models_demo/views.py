from django.shortcuts import render, redirect, get_object_or_404
from models_demo.models import Article

# Create your views here.


def home(request):
    reading_data = Article.objects.all()
    return render(request, 'home.html', {'data': reading_data})


def loginpage(request):
    if request.method == 'POST':
        title_data = request.POST['title']
        desc_data = request.POST['desc']

        # first method
        # a = Article(title=title_data, desc=desc_data)
        # a.save()

        # second method
        Article.objects.create(title=title_data, desc=desc_data)
        # this is the name which you written in path()
        return redirect('homepage')
    return render(request, 'loginpage.html')

# Add function (currently unused)


def add(request):
    print(request.POST)

# update function


def edit(request, pk):
    article = get_object_or_404(Article, id=pk)

    if request.method == 'POST':
        new_title = request.POST.get('title')
        new_desc = request.POST.get('desc')

        if new_title and new_desc:
            article.title = new_title
            article.desc = new_desc
            article.save()
            return redirect('homepage')
    return render(request, 'edit.html', {'editing': article})


def deleteit(request, pk):
    data = get_object_or_404(Article, id=pk)
    data.delete()
    return redirect('homepage')
