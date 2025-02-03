'''
from django.contrib import admin
from django.urls import path

from app1 import views
# from app2 import views  # this will override above views file
from app2 import views as electronics

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('about/', views.about),

    # path('mobiles/', views.mobiles)
    # since app1's views is overridden by app2's views, home fn is not present in app2 view; home/ NOT WORKING

    # solution: use alias for second view during imoporting, now it works
    path('mobiles/', electronics.mobiles)
]
'''


# DAY15: sir today taught us to use APP LEVEL URL file,
# so from now consider the below code (above code is for understanding)
# refer day15 notes for better understanding


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('app1.urls')),
    path('app2/', include('app2.urls')),
    path('app3/', include('app3.urls')),
    path('app4/', include('app4.urls')),
    path('app5/', include('app5.urls')),
]
