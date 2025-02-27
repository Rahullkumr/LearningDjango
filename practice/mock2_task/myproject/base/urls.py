from django.urls import path
from base import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('registration', views.reg_form, name='reg_form'),
    path('studentlist', views.stu_list, name='stu_list'),
    path('details/<int:primary_key>', views.details, name='details'),
]
