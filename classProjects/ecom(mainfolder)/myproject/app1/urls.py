from django.urls import path
from app1 import views

urlpatterns = [
    path('home', views.home),
    path('about', views.about),
    path('electronics', views.electronics),
    path('mobile', views.mobile),
]
