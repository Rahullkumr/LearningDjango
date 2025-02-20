from django.urls import path
from fashion import views

urlpatterns = [
    path('', views.fashion_home),
    path('accessories', views.accessories),
    path('clothing', views.clothing),
    path('shoes', views.shoes),
]
