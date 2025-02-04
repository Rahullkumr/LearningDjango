from django.urls import path
from app1 import views

urlpatterns = [
    path('views1', views.homepage),
    path('views2', views.about),
    path('views3', views.contact),
    path('views4', views.help),
    path('views5', views.product),
]
