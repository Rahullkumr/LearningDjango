from django.urls import path
from app2 import views

urlpatterns = [
    path('mobile', views.mobile),
    path('charger', views.charger),
    path('cable', views.cable),
    path('earphone', views.earphone),
    path('headphone', views.headphone),
]
