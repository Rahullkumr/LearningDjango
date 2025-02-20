from django.shortcuts import render

# Create your views here.


def sports_home(request):
    return render(request, 'sports_html/sports_home.html')


def cricket(request):
    cricket_data = [
        {
            'brand': 'PowerBat',
            'type': 'Cricket Bat',
            'price': 7500,
            'color': 'Wooden Brown'
        },
        {
            'brand': 'SpeedBall',
            'type': 'Cricket Ball',
            'price': 1200,
            'color': 'Red'
        },
        {
            'brand': 'ShieldPro',
            'type': 'Batting Pads',
            'price': 3500,
            'color': 'White'
        },
        {
            'brand': 'GripMaster',
            'type': 'Batting Gloves',
            'price': 1800,
            'color': 'Black & White'
        },
    ]
    context = {'cricket_data': cricket_data}
    return render(request, 'sports_html/cricket.html', context)


def badminton(request):
    badminton_data = [
        {
            'brand': 'SmashAce',
            'type': 'Badminton Racket',
            'price': 5000,
            'color': 'Black & Yellow'
        },
        {
            'brand': 'FeatherLite',
            'type': 'Shuttlecock',
            'price': 800,
            'color': 'White'
        },
        {
            'brand': 'GripMax',
            'type': 'Badminton Shoes',
            'price': 4000,
            'color': 'Blue'
        },
        {
            'brand': 'SwiftMove',
            'type': 'Badminton Bag',
            'price': 2200,
            'color': 'Red & Black'
        },
    ]
    context = {'badminton_data': badminton_data}
    return render(request, 'sports_html/badminton.html', context)


def football(request):
    football_data = [
        {
            'brand': 'KickMaster',
            'type': 'Football',
            'price': 3000,
            'color': 'White & Black'
        },
        {
            'brand': 'GoalPro',
            'type': 'Football Shoes',
            'price': 4500,
            'color': 'Red & White'
        },
        {
            'brand': 'DefenderX',
            'type': 'Shin Guards',
            'price': 1500,
            'color': 'Black'
        },
        {
            'brand': 'StrikerFit',
            'type': 'Football Jersey',
            'price': 2500,
            'color': 'Blue & White'
        },
    ]
    context = {'football_data': football_data}
    return render(request, 'sports_html/football.html', context)
