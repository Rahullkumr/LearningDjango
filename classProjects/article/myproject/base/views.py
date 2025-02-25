from django.shortcuts import render

# Create your views here.

articles_data = [
    {
        'id': 1,
        'title': 'Indian economics',
        'desc': '''
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Id odit modi ea quod, ratione necessitatibus quos sit expedita laboriosam veniam, voluptatibus alias unde explicabo quidem provident dolor dignissimos omnis vero minus dolorem ullam? Tempora magni laboriosam placeat earum, quisquam quia iure qui ullam accusantium harum, rerum soluta expedita sint rem.
        '''
    },
    {
        'id': 2,
        'title': 'Indian Transport',
        'desc': '''
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Id odit modi ea quod, ratione necessitatibus quos sit expedita laboriosam veniam, voluptatibus alias unde explicabo quidem provident dolor dignissimos omnis vero minus dolorem ullam? Tempora magni laboriosam placeat earum, quisquam quia iure qui ullam accusantium harum, rerum soluta expedita sint rem.
        '''
    },
    {
        'id': 3,
        'title': 'Indian Crops',
        'desc': '''
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Id odit modi ea quod, ratione necessitatibus quos sit expedita laboriosam veniam, voluptatibus alias unde explicabo quidem provident dolor dignissimos omnis vero minus dolorem ullam? Tempora magni laboriosam placeat earum, quisquam quia iure qui ullam accusantium harum, rerum soluta expedita sint rem.
        '''
    },
    {
        'id': 4,
        'title': 'Indian Tourism',
        'desc': '''
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Id odit modi ea quod, ratione necessitatibus quos sit expedita laboriosam veniam, voluptatibus alias unde explicabo quidem provident dolor dignissimos omnis vero minus dolorem ullam? Tempora magni laboriosam placeat earum, quisquam quia iure qui ullam accusantium harum, rerum soluta expedita sint rem.
        '''
    },
    {
        'id': 5,
        'title': 'Indian Defence',
        'desc': '''
            Lorem ipsum, dolor sit amet consectetur adipisicing elit. Id odit modi ea quod, ratione necessitatibus quos sit expedita laboriosam veniam, voluptatibus alias unde explicabo quidem provident dolor dignissimos omnis vero minus dolorem ullam? Tempora magni laboriosam placeat earum, quisquam quia iure qui ullam accusantium harum, rerum soluta expedita sint rem.
        '''
    },
]


def home(request):
    context = {
        'indian_data': articles_data,
    }
    return render(request, 'home.html', context)


def events(request):
    return render(request, 'events.html')


def news(request):
    return render(request, 'news.html')


def about(request):
    return render(request, 'about.html')


def read(request, recieved_button_ka_id):
    # print(type(int(primary_key)))

    for i in articles_data:
        if i['id'] == recieved_button_ka_id:
            context = {'primary_key': i}

    return render(request, 'read.html', context)
