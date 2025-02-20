from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    # print('hello world')
    # return HttpResponse('homepage')

    # today learnt about templates, so we will use below code

    a = 'data from home page'
    # context = {'home_data': a}

    d = [
        # we will get this type of list of dictionaries from db
        {'name': 'Rahul', 'rollno': 15, 'current_city': 'Pune', 'state': 'Maharashtra'}
    ]
    context = {'home_data': d}
    return render(request, 'all_temp1/home.html', context)


def about(request):
    # return HttpResponse('about page')

    cdata = [
        {'name': 'India', 'capital': 'New Delhi'},
        {'name': 'Nepal', 'capital': 'Kathmandu'},
    ]
    context = {'countries_data': cdata}
    # context = {'countries_data': cdata, 'new_contextdata': 9999}
    return render(request, 'all_temp1/about.html', context)


def electronics(request):
    context = {
        'electronics_data': ['mobiles', 'charger', 'earphone', 'television', 'fridge', 'sound box', 'projector', 'AC']
    }
    return render(request, 'all_temp1/electronics.html', context)


def mobile(request):
    context = {
        'mobile_data': ['Samsung', 'Apple', 'Micromax', 'Redmi', 'Oppo', 'Motorolla', 'Nothing']
    }
    return render(request, 'all_temp1/mobile.html', context)
