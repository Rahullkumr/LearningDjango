from django.urls import path
from app8 import views


urlpatterns = [
    path('views1', views.red),
    path('views2', views.green),
    path('views3', views.blue),
    path('views4', views.yellow),
    path('views5', views.violet),
    path('views6', views.magenta),
    path('views7', views.chocolate),
    path('views8', views.black),
    path('views9', views.white),
    path('views10', views.gray),
]
