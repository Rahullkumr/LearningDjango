from django.shortcuts import render

# Create your views here.


def electro_home(request):
    return render(request, 'electro_html/electro_home.html')


def mobile(request):
    data = [
        {
            # 'img_link': 'https://b2c-contenthub.com/wp-content/uploads/2024/10/Galaxy-A16-5G-2.webp?w=1200',
            'company': 'Samsung',
            'model': 'Galaxy A17',
            'price': 25000,
            'color': 'Black'
        },
        {
            # 'img_link': '',
            'company': 'Apple',
            'model': 'Iphone 16 pro',
            'price': 60000,
            'color': 'Dark Gray'
        },
        {
            # 'img_link': '',
            'company': 'Lava',
            'model': 'Agni 2',
            'price': 12000,
            'color': 'Red'
        },
        {
            # 'img_link': '',
            'company': 'Redmi',
            'model': 'Note 10 pro',
            'price': 20000,
            'color': 'Silver'
        },
    ]
    context = {'mobile_data': data}
    return render(request, 'electro_html/mobile.html', context)


def laptop(request):
    laptop_data = [
        {
            'company': 'Dell',
            'model': 'XPS 15',
            'price': 125000,
            'storage': '512GB SSD'
        },
        {
            'company': 'Apple',
            'model': 'MacBook Pro',
            'price': 169000,
            'storage': '1TB SSD'
        },
        {
            'company': 'HP',
            'model': 'Pavilion Gaming',
            'price': 85000,
            'storage': '512GB SSD'
        },
        {
            'company': 'Asus',
            'model': 'ROG Strix',
            'price': 145000,
            'storage': '1TB SSD'
        }
    ]
    context = {'laptop_data': laptop_data}
    return render(request, 'electro_html/laptop.html', context)


def tv(request):
    tv_data = [
        {
            'company': 'Samsung',
            'model': 'Neo QLED 4K',
            'price': 89999,
            'size': '55 inch',
        },
        {
            'company': 'LG',
            'model': 'OLED C3',
            'price': 149999,
            'size': '65 inch',
        },
        {
            'company': 'Sony',
            'model': 'Bravia XR',
            'price': 79999,
            'size': '50 inch',
        },
        {
            'company': 'Mi',
            'model': 'Q1 Series',
            'price': 59999,
            'size': '55 inch',
        }
    ]
    context = {'tv_data': tv_data}
    return render(request, 'electro_html/tv.html', context)
