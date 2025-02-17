from django.urls import path
from . import views

urlpatterns = [
    path('fighter_jets', views.fighter_jets, name='fj'),
    path('missiles', views.air_missiles, name='am'),
    path('drones', views.drones, name='drones'),
    path('helicopters', views.helicopters, name='helicopters'),
]
