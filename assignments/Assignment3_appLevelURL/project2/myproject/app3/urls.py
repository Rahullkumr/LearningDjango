from django.urls import path
from app3 import views

urlpatterns = [
    path('views1', views.about),
    path('views2', views.contact),
    path('views3', views.homepage),
    path('views4', views.help),
    path('views5', views.product),
]
