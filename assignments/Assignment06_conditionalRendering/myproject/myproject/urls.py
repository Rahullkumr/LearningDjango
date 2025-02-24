
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('air/', include('air.urls')),
    path('water/', include('water.urls')),
    path('land/', include('land.urls')),
]
