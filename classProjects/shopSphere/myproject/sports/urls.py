from django.urls import path
from . import views

urlpatterns = [
    path('', views.sports_home),
    path('cricket', views.cricket),
    path('badminton', views.badminton),
    path('football', views.football),
]
