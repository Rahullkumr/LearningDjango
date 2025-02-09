from django.urls import path

from app9 import views

urlpatterns = [
    path('submarine', views.submarine),
    path('missile', views.missile),
    path('fighterjet', views.fighterjet),
    path('helicopter', views.helicopter),
    path('rocket', views.rocket),
]
