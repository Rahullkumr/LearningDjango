from django.urls import path
from base import views

urlpatterns = [
    path('students', views.students),
    path('student/<int:pk>', views.student),
]
