from django.urls import path
from app4 import views

urlpatterns = [
    path('views1', views.homepage),
    path('views2', views.about),
    path('views3', views.contact),
    path('views4', views.helppage),
    path('views5', views.product),
    path('views6', views.contact),
    path('views7', views.category),
    path('views8', views.checkout),
    path('views9', views.comparision),
    path('views10', views.recommendation),
]
