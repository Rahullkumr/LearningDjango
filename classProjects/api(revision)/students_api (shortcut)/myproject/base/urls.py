from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.students),
    path('student/<int:pk>', views.student),
]
