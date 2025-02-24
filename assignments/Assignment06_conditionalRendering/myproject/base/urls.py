from django.urls import path
from base import views

urlpatterns = [
    path('', views.homepage, name='')
    # path('', views.homepage, name='homepage')
]
