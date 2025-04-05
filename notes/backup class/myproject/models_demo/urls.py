from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.deleteit, name='deleteit'),
]
