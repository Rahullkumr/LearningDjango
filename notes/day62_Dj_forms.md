# Day 61: 10 April 2025 

- Django Forms start

## Steps

- Create a basic Dj project with an app (say base)

- create base>forms.py and create a form class

    ```py
    class Student(forms.Form):
        sname = forms.CharField(max_length=100)
        semail = forms.EmailField()
    ```

- create view to handle form
    - import form class
    - create context and pass it
    - use context key to access form in the template

- Create template to render the form and other html

- configure urls

- run server and hit the localhost url

## 4 ways to render the Dj form in html file

1. Default way

2. By using  .as_p

3. Using for loop ✅

4. Manually rendering 