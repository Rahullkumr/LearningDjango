from django.urls import path
from app2 import views

urlpatterns = [
    path('home', views.home),
    path('circle', views.circle),
    path('square', views.square),
    path('rectangle', views.rectangle),
]
