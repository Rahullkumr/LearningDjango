# Day 26: 15 Feb 2025

> Dynamic Routing

- Till now we achieved Dynamic Routing using `<a href='url'>`

- But it will not work if the port number is changed

- So we need to use `url dtl tag` instead of `<a href='url'>`

- syntax

    ```django 
    {% url 'pathname' %}
    ```

- Examples

    ```django
    <!-- Instead of this (manual routing) -->
    <a href="http://127.0.0.1:8000/electronics/">Electronics</a>

    <!-- Use this (dynamic routing) -->
    <a href="{% url 'electronics' %}">Electronics</a>

    <!-- For URLs with parameters -->
    <a href="{% url 'product_detail' product.id %}">{{ product.name }}</a>
    ```
    ```py
    # urls.py 

    from django.urls import path
    urlpatterns = [
        path('electronics/', views.electronics, name='electronics'),    # pathname (url dtl tag) == name
        path('product/<int:id>/', views.product_detail, name='product_detail'),
    ]
    ```

## Assignment

- Assignment05 

    - Do a project that includes all concepts till dynamic routing

    - do DEFENCE related