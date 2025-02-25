# Day 33: 25 Feb 2025

> Article Project

- In this project we learnt how to pass data from one template to another template

## Concepts used: 

1. url dtl tag

    ```django html
    <a href="{% url 'read' i.id %}">
        <button>Read</button>
    </a>
    ```

2. path converter

    ```py
    path('read/<int:primary_key>', views.read, name='read'),

    # <int:primary_key> is the path converter
    ```

3. argument

    ```django
    <a href="{% url 'read' i.id %}">

    # here i.id is the argument
    ```

4. context  

    ```py
    def read(request, primary_key):
        for i in articles_data:
            if i['id'] == primary_key:
                context = {'primary_key': i}
        return render(request, 'read.html', context)
    ```

5. Truncatewords

    ```django html
    <p>{{i.desc | truncatewords:20}}</p>
    ```