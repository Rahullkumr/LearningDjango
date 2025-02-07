from django.urls import path
from app3 import views

urlpatterns = [
    path('red', views.red),
    path('green', views.green),
    path('blue', views.blue),
]
