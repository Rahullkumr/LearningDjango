from django.urls import path
from . import views

urlpatterns = [
    path('', views.electro_home, name='electro_home'),
]
