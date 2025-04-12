from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.deletepage, name='deletepage'),
]
