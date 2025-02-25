from django.urls import path
from base import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('events', views.events, name='events'),
    path('news', views.news, name='news'),
    path('about', views.about, name='about'),
    path('read/<int:primary_key>', views.read, name='read'),
]
