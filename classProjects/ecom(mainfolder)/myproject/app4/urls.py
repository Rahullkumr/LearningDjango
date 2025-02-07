from django.urls import path
from app4 import views

urlpatterns = [
    path('sachin', views.Sachin),
    path('dhoni', views.Dhoni),
    path('virat', views.Virat),
]
