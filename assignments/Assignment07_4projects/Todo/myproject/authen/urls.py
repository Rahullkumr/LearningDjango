from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name='loginpage'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
]
