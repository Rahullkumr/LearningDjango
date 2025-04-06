from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('registration/', views.registration, name='registration'),
]
