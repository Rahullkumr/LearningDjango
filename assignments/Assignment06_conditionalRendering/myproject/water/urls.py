from django.urls import path
from . import views

urlpatterns = [
    path('', views.water_home, name='water_home'),
    path('fish', views.fish, name='fish'),
    path('ship', views.ship, name='ship'),
    path('yacht', views.yacht, name='yacht'),
]
