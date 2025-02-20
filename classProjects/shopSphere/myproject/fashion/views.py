from django.shortcuts import render

# Create your views here.


def fashion_home(request):
    return render(request, 'fashion_html/fashion_home.html')


def accessories(request):
    accessories_data = [
        {
            'brand': 'EliteWear',
            'type': 'Wrist Watch',
            'price': 5000,
            'color': 'Silver'
        },
        {
            'brand': 'TrendX',
            'type': 'Sunglasses',
            'price': 3000,
            'color': 'Black'
        },
        {
            'brand': 'Glamura',
            'type': 'Handbag',
            'price': 2500,
            'color': 'Brown'
        },
        {
            'brand': 'BoldStyle',
            'type': 'Leather Belt',
            'price': 500,
            'color': 'Dark Brown'
        },
    ]
    context = {'accessories_data': accessories_data}
    return render(request, 'fashion_html/accessories.html', context)


def clothing(request):
    clothing_data = [
        {
            'brand': 'StyleTrend',
            'type': 'T-Shirt',
            'price': 800,
            'color': 'Black'
        },
        {
            'brand': 'UrbanVogue',
            'type': 'Hoodie',
            'price': 1300,
            'color': 'Gray'
        },
        {
            'brand': 'DenimCraze',
            'type': 'Jeans',
            'price': 1700,
            'color': 'Blue'
        },
        {
            'brand': 'FitFlex',
            'type': 'Track Pants',
            'price': 600,
            'color': 'Navy Blue'
        },
    ]
    context = {'clothing_data': clothing_data}
    return render(request, 'fashion_html/clothing.html', context)


def shoes(request):
    shoes_data = [
        {
            'brand': 'Nike',
            'model': 'Air Max 270',
            'price': 5000,
            'color': 'Black & White'
        },
        {
            'brand': 'Adidas',
            'model': 'UltraBoost 22',
            'price': 7500,
            'color': 'Blue'
        },
        {
            'brand': 'Puma',
            'model': 'RS-X',
            'price': 3000,
            'color': 'Red & Black'
        },
        {
            'brand': 'Rebook',
            'model': 'Nano X3',
            'price': 800,
            'color': 'Gray'
        },
    ]
    context = {'shoes_data': shoes_data}
    return render(request, 'fashion_html/shoes.html', context)
