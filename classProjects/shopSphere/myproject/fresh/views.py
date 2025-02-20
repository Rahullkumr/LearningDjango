from django.shortcuts import render

# Create your views here.


def home(request):
    context = {
        'page_name': 'homepage',
    }
    return render(request, 'fresh_html/fresh_home.html', context)


def carrot(request):
    carrot_data = {
        'price': 'RS 50',
        'quantity': 100,
        'company': 'Fresh Veg Ltd',
    }
    context = {'page_name': 'Carrot', 'carrot_data': carrot_data}
    return render(request, 'fresh_html/carrot.html', context)


def cucumber(request):
    cucumber_data = {
        'price': 'RS 40',
        'quantity': 30,
        'company': 'Fresh Cucumber adn comp',
    }
    context = {'page_name': 'Cucumber', 'cucumber_data': cucumber_data}
    return render(request, 'fresh_html/cucumber.html', context)


def tomato(request):
    tomato_data = {
        'price': 'RS 30',
        'quantity': 10,
        'company': 'Fresh Red Ltd',
    }
    context = {'page_name': 'Tomato', 'tomato_data': tomato_data}
    return render(request, 'fresh_html/tomato.html', context)
