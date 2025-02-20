from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('carrot', views.carrot),
    path('cucumber', views.cucumber),
    path('tomato', views.tomato),
]
