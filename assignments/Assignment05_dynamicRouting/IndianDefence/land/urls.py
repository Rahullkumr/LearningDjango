from django.urls import path
from . import views

urlpatterns = [
    path('tanks', views.tanks, name='tanks'),
    path('land_missiles', views.land_missiles, name='lm'),
    path('air_defence_sys', views.air_defence_sys, name='ads'),
    path('radars', views.radars, name='radars'),
]
