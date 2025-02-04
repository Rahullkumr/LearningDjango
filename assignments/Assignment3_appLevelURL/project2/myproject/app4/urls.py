from django.urls import path
from app4 import views

urlpatterns = [
    path('views1', views.about),
    path('views2', views.contact),
    path('views3', views.help),
    path('views4', views.homepage),
    path('views5', views.product),
]