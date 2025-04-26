from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage, name='loginpage'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('changepass/', views.changepass, name='changepass'),
    path('logout/', views.logout, name='logout'),
]
