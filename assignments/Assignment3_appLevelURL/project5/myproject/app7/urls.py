from django.urls import path
from app7 import views

urlpatterns = [
    path('andhrapradesh', views.AndhraPradesh),
    path('bihar', views.Bihar),
    path('chandigarh', views.Chandigarh),
    path('delhi', views.Delhi),
    path('haryana', views.Haryana),
    path('jharkhand', views.Jharkhand),
    path('maharashtra', views.Maharashtra),
    path('orissa', views.Orissa),
    path('telangana', views.Telangana),
    path('mizoram', views.Mizoram),
]
