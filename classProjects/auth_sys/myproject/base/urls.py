from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('about/', views.about, name='aboutpage'),
    path('profile/', views.profile, name='profilepage'),
    path('register/', views.register, name='registerpage'),
    path('login/', views.login, name='loginpage'),
    path('logout/', views.logout, name='logoutpage'),
]
