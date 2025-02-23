from django.urls import path
from . import views

urlpatterns = [
    path("", views.land_home, name='land_home'),
    path("tiger", views.tiger, name='tiger'),
    path("bus", views.bus, name='bus'),
    path("train", views.train, name='train')
]
