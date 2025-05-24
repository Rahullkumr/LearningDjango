

from django.urls import path
from . import views

urlpatterns=[
    path('login_',views.login_,name='login_'),
    path('register',views.register,name='register'),
    path('logout_',views.logout_,name='logout_'),
    path('profile',views.profile,name='profile'),
    path('changepass',views.changepass,name='changepass'),
]