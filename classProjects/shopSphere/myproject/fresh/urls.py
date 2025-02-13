from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('carrot', views.carrot),
    path('cucumber', views.cucumber),
    path('fresh_about', views.fresh_about),
    path('tomato', views.tomato),
    path('fresh_cart', views.fresh_cart),
]
