
from django.contrib import admin
from django.urls import path
from pro02_app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fun1/', views.fun1),
    path('fun2/', views.fun2),
    path('fun3/', views.fun3),
    path('fun4/', views.fun4),
    path('fun5/', views.fun5),
    path('fun6/', views.fun6),
    path('fun7/', views.fun7),
    path('fun8/', views.fun8),
    path('fun9/', views.fun9),
    path('fun10/', views.fun10),

    path('fun11/', views.fun11),
    path('fun12/', views.fun12),
    path('fun13/', views.fun13),
    path('fun14/', views.fun14),
    path('fun15/', views.fun15),
    path('fun16/', views.fun16),
    path('fun17/', views.fun17),
    path('fun18/', views.fun18),
    path('fun19/', views.fun19),
    path('fun20/', views.fun20),

    path('fun21/', views.fun21),
    path('fun22/', views.fun22),
    path('fun23/', views.fun23),
    path('fun24/', views.fun24),
    path('fun25/', views.fun25),
]
