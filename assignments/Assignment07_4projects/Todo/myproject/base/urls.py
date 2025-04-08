from django.urls import path, include
from . import views

urlpatterns = [
    path('alltasks/', views.alltasks, name='alltasks'),
    path('addtask/', views.addtask, name='addtask'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
