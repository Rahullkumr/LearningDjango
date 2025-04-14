from django.urls import path
from base import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about', views.about, name='about'),
    path('read/<int:recieved_button_ka_id>', views.read, name='read'),
    path('search/', views.search, name='search'),
]
