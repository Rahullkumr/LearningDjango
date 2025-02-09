from django.urls import path
from app8 import views

urlpatterns = [
    path('about', views.about),
    path('contact', views.contact),
    path('helpage', views.helpage),
    path('home', views.home),
    path('testimony', views.testimony),
]
