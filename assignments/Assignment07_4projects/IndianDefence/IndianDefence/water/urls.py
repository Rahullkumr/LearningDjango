from django.urls import path
from . import views

urlpatterns = [
    path('submarines', views.submarines, name='submarines'),
    path('aircraft_carriers', views.aircraft_carriers, name='ac'),
    path('destroyers', views.destroyers, name='destroyer'),
    path('frigates', views.frigates, name='frigate'),
]
