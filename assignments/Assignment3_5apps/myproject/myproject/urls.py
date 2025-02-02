"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views 
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views 
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf 
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views as app1views
from app2 import views as app2views
from app3 import views as app3views
from app4 import views as app4views
from app5 import views as app5views

urlpatterns = [
    path('admin/', admin.site.urls),

    # app1 views
    path('app1fun1/', app1views.fun1),
    path('app1fun2/', app1views.fun2),
    path('app1fun3/', app1views.fun3),
    path('app1fun4/', app1views.fun4),
    path('app1fun5/', app1views.fun5),

    # app2 views
    path('app2fun1/', app2views.fun1),
    path('app2fun2/', app2views.fun2),
    path('app2fun3/', app2views.fun3),
    path('app2fun4/', app2views.fun4),
    path('app2fun5/', app2views.fun5),

    # app3 views
    path('app3fun1/', app3views.fun1),
    path('app3fun2/', app3views.fun2),
    path('app3fun3/', app3views.fun3),
    path('app3fun4/', app3views.fun4),
    path('app3fun5/', app3views.fun5),

    # app4 views
    path('app4fun1/', app4views.fun1),
    path('app4fun2/', app4views.fun2),
    path('app4fun3/', app4views.fun3),
    path('app4fun4/', app4views.fun4),
    path('app4fun5/', app4views.fun5),

    # app5 views
    path('app5fun1/', app5views.fun1),
    path('app5fun2/', app5views.fun2),
    path('app5fun3/', app5views.fun3),
    path('app5fun4/', app5views.fun4),
    path('app5fun5/', app5views.fun5),

]
