from django.urls import path
from air import views

urlpatterns = [
    path('', views.air_home, name='air_home'),
    path('birds', views.birds, name='birds'),
    path('helicopter', views.helicopter, name='helicopter'),
    path('aeroplane', views.aeroplane, name='aeroplane'),
]
