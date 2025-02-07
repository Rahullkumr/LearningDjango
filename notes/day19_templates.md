# Day19: 07-Feb-2025

> templates

## Templates

- used to separate business logic and html code 

- Two types of templates:

    - App level templates

    - Project level templates

## App level templates

- create a **`templates > all_temp1`** folder inside app1 

    - it'll contain all html files (template)

- we don't call them that:

    ```
    fns     ➡️ views like about views
    urls    ➡️ path 
    html    ➡️ template like home template
    ```

- How to send request to template and render it?

    - using `render()` method

    - render() takes two arguments:
        - request
        - 'path_of_template_file'


    ```py
    from django.shortcuts import render

    def home(request):
        return render(request, 'all_temp1/home.html')
    ```

```diff
- Template doesn't exist

when we don't write the folder name or template name correctly
```

### Flow of request

browser ➡️ urls.py (main) ➡️ urls.py (app level) ➡️ views.py ➡️ templates