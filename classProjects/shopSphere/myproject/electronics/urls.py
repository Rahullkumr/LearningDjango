from django.urls import path
from . import views

urlpatterns = [
    path('', views.electro_home),
    path('laptop', views.laptop),
    path('mobile', views.mobile),
    path('tv', views.tv),
    path('electro_about', views.electro_about),
    path('electro_cart', views.electro_cart),
]
