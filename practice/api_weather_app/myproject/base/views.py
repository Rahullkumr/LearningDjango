import requests
from django.shortcuts import render


def get_weather_data(city):
    API_KEY = '750635eec70fd16a4046f77ad926d593'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            'city': data['name'],
            'condition': data['weather'][0]['description'].capitalize(),
            'temperature': data['main']['temp'],
            'feels_like': data['main']['feels_like'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'cloud_coverage': data['clouds']['all'],
            'icon': data['weather'][0]['icon'],
        }
        return weather
    return None


def homepage(request):
    weather_data = None
    if request.method == 'POST':
        city = request.POST.get('city')
        weather_data = get_weather_data(city)
    return render(request, 'homepage.html', {'weather': weather_data})
