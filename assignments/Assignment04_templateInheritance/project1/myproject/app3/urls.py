from django.urls import path

from app3 import views

urlpatterns = [
    path('shirt', views.shirt),
    path('pant', views.pant),
    path('coat', views.coat),
    path('shoe', views.shoe),
    path('sweater', views.sweater),
]
