from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name='loginpage'),
    path('register', views.register, name='register'),
    path('logoutme', views.logoutme, name='logoutme'),
    path('profile/', views.profile, name='profile'),
    path('profile/changepass/', views.changepass, name='changepass'),
    path('updateprofile/<int:pk>', views.updateprofile, name='updateprofile'),
    path('about', views.about, name='about'),
]
