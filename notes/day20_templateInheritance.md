# Day20: 08-Feb-2025

> Template Inheritance

## Template Inheritance

- In all templates i.e html files, the boilerplate code is common means repeated.

- Django follows DRY (Don't Repeat Yourself)

- So to avoid this code repetation, we create a `main.html` file which will contain the boiler plate code.

- This way we achieve code reusability and template Inheritance

- **Template Inheritance** is the replication of one template for another template 

- `dtl tag` Django Template Language tag is used to inject unique code

- Eg: 

    ```
    {% block content %}

    {% endblock content %}
    ```

## Implementation of Template Inheritance

- Create **templates > main.html (parent template bolenge)** 

    -  write the boiler plate code here, code will be injected in this template

- ### main.html

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>document</title>
    </head>
    <body>
        <h1>this is main.html template boiler plate</h1>
        {% block content %} 
        
        {% endblock content %}
    </body>
    </html>
    ```

- Create **templates > all_temp1 > home.html (child template bolenge)** 

    - this page will extend main.html (Inheritance)

    - write the home specific code here which will be injected into main.html 

- ### home.html

    ```html 
    {% extends 'main.html' %}

    {% block content%}
        <h2>this is homepage</h2>
    {% endblock content%}
    ```

## Assignment

> Assignment04_templateInheritance

- Create 2 projects 10 apps each with 5 views in each app 
- Implement template Inheritance (common boilerplate code)