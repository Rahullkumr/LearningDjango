# Day15: 03-Feb-2025

> app level urls.py file

- app level url file, why?
    - to organise the path related to that app

- will never use main url file which is present in app config folder (`you must know which folder it is`) 

- and also import the views in app level url file only



- This is app level url (in app1's urls.py) file:

    ```
    from django.urls import path
    from app1 import views

    urlpatterns = [
        path('home', views.home),
        path('about', views.about),
    ]
    ```

## How to connect **app level url** to **main url** ?

- use include() method in main url file

    - `from django.urls import path, **include**`

- in main url file, write 

    ```
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('app1/', include('app1.urls')),
    ]
    ```

## Assignment 3

- Two projects, create 5 apps, each app 5 views and app level url file