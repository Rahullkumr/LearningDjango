from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name='loginpage'),
    path('register/', views.register, name='register'),
    path('logoutme/', views.logoutme, name='logoutme'),
]
