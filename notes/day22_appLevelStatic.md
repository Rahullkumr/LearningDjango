# Day22: 11-Feb-2025

- app level static file for css

- load static dtl tag is used to load external css file

    ```
    <!-- write this in main.html -->

    {% load static %} ===> used to load static files

    <link rel='stylesheet' href="{% static 'style.css' %}">
    ```


- django is for backend that we write in views, models

- it considers views as main file

- `render()`
    - two mandatory args: 
        - request
        - path of template

    - used to render templates and also to create response