from django.urls import path
from . import views

urlpatterns = [
    path('', views.electro_home),
    path('laptop', views.laptop),
    path('mobile', views.mobile),
    path('tv', views.tv),
]
