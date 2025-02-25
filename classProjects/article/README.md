# Article Project

```diff
+ learnt to pass data from one template to another template
```

> When you click on the button of a particular article in **home.html**, the data of that article should be sent to **read.html** template and displayed there.

## STEPS to achieve this:


1. Go to **home.html** (template jaha se data bhejna hai)

    - Each article has its own `id`, so pass it as the argument in `url dtl tag`

    - so when the *read* button will be clicked the data will be passed to next step.

        ```django html
        <a href="{% url 'read' i.id %}"> <button>Read</button> </a>
        ```
    - a/c to the above code, data (i.e id) will pass to the route whose name is **read** 

2. app level url (urls.py)

    - `path converter` concept is used here

        ```py
        path('read/<int:recieved_button_ka_id>', views.read, name='read'),

        # <int:recieved_button_ka_id> is the path converter
        ```

    - the path will be converted a/c to the data
        
        - if 2nd article's button is clicked then path/link in the browser will look like this **`read/2`**

    - then the data will travel to the `views.read` view 

3. views.py 

    - here the **data is recieved in parameter**

        ```py
            def read(request, recieved_button_ka_id)
        ```

    - **Creation of context** 
    
        - context will be the entire article which matches the button id
        
        - pass the context to `read.html` template

        ```py
        def read(request, recieved_button_ka_id):
            for i in articles_data:
                if i['id'] == recieved_button_ka_id:
                    context = {'primary_key': i}
            return render(request, 'read.html', context)
        ```

4. read.html (template jaha par data ko recieve and display karna hai)

    - since the entire article is recieved as context, we can use the following code to display it:

    ```django html
        <h1>{{primary_key.title}}</h1>
        <p>{{primary_key.desc}}</p>
        <a href="{% url 'homepage' %}">
            <button>Go back</button>
        </a>
    ``` 

## Extra learnings

- uppercase

    ```django html
    <h3>{{i.title | upper}}</h3>
    ```

- Truncatewords

    ```django html
    <p>{{i.desc | truncatewords:20}}</p>
    ```
