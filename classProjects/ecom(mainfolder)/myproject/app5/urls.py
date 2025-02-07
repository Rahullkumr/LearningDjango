from django.urls import path
from app5 import views

urlpatterns = [
    path('aeroplane', views.aeroplane),
    path('train', views.train),
    path('ship', views.ship),
]
