from django.urls import path

from app4 import views

urlpatterns = [
    path('car', views.car),
    path('bike', views.bike),
    path('rickshaw', views.rickshaw),
    path('bicycle', views.bicycle),
    path('truck', views.truck),
]
