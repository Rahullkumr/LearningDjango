from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginauth, name='loginauth'),
    path('register/', views.register, name='registerpage'),
    path('logoutpage/', views.logoutpage, name='logoutpage'),
    path('profile/', views.profile, name='profile'),
    path('changepass/', views.changepass, name='changepass'),
]
