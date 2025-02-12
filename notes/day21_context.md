# Day21: 10-Feb-2025

> send data from views to template

- block dtl tag is used to inject unique code in main.html

- navbar in main.html

- remove navbar code from main.html and create navbar.html with main.html

- use `{% include 'navbar.html' %}` dtl tag to include navbar in main.html

- default route to render app1

- to avoid mess, we keep the all_tempsN decent and clean 

- we will never write unique data in templates rather we will send the data from views


- data present in db --> views to apply logic --> child templates

## How to send data from views to templates 

- using context 

- pass: 
    - a string 
    - a list
        - using indexing 
        - looping 

    - dictionary
    - list of dictionary (pass this only)

- use dtl tags like **for**, **variable i.e {{key_of_context}}** for showing the context data in respective templates.

```
{% for stmt %} 

{% endfor %},

{{key_of_context}},
```

## Examples 

1. Send and display a `string`, a `list` and a `dictionary`

    ```py
    views.py

    from django.shortcuts import render

    def home(request):
        context = {
            'string_data': 'Hello, World', 
            'list_data': [1,2,3,4,5],
            'dict_data': { 
                'name': 'Sukhoi', 
                'type': 'Defence,
            },
        }
        return render(request, 'home.html', context)
    ```

    ```django html
    home.html

    <h2>String Data</h2>

        <h1>{{ string_data }}</h1> 



    <h2>List Data</h2>

        <p>{{list_data.0}}</p>
        <ul>
            {% for item in list_data %}
                <li>{{ item }}</li>
            {% endfor %}
        </ul>



    <h2>Dictionary Data</h2>
        <p>{{dict_data}}</p>
        <p>Name: {{ dict_data.name }}</p>
        <p>Type: {{ dict_data.type }}</p>


    ```

2. Send and display a `list of dictionaries`

    ```py
    views.py

    from django.shortcuts import render

    def home(request):
        context = {
            'list_of_dicts': [
                {'name': 'Sukhoi', 'type': 'Defence' },
                {'name': 'Indigo', 'type': 'Passenger' },
                {'name': 'Boeing', 'type': 'Cargo' }
            ],
        }
        return render(request, 'home.html', context)
    ```

    ```django html
    home.html

    <h2>List of Dictionaries Data</h2>
        <ul>
            {% for plane in list_of_dicts %}
                <li>Name: {{ plane.name }} and Type: {{ plane.type }}</li>
            {% endfor %}
        </ul>
    ```



## Note

> Data from database comes in the form of **list of dictionaries**