from django.urls import path, include
from . import views

urlpatterns = [
    path('alltasks/', views.alltasks, name='alltasks'),
    path('addtask/', views.addtask, name='addtask'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),

    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('loginpage/', views.loginpage, name='loginpage'),
    path('logout/', views.logout, name='logout'),
]
