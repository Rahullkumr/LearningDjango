from django.urls import path
from app5 import views


urlpatterns = [
    path('views1', views.about),
    path('views2', views.help),
    path('views3', views.homepage),
    path('views4', views.contact),
    path('views5', views.product),
]
