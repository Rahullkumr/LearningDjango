from django.urls import path
from base import views
from air import views as air_views
from water import views as water_views
from land import views as land_views

urlpatterns = [
    path('', views.home, name='home'),
    path('air', air_views.fighter_jets, name='air'),
    path('water', water_views.submarines, name='water'),
    path('land', land_views.tanks, name='land'),
]
