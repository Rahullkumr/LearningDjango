from django.urls import path

from app2 import views

urlpatterns = [
    path('blue', views.blue),
    path('green', views.green),
    path('red', views.red),
    path('white', views.white),
    path('yellow', views.yellow),
]
