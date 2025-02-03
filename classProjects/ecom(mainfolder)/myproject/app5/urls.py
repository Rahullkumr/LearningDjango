from django.urls import path
from app5 import views

urlpatterns = [
    path('views1', views.views1),
    path('views2', views.views2),
    path('views3', views.views3),
    path('views4', views.views4),
    path('views5', views.views5),
]
