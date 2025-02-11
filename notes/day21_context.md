# Day21: 10-Feb-2025

> send data from views to template

- block dtl tag is used to inject unique code in main.html

- navbar in main.html

- remove navbar code from main.html and create navbar.html with main.html

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

- use dtl tags like **include**, **for** for showing the context data in respective templates.

```
{% include 'navbar.html' %}
{% for stmt %} code {% endfor %},
{{}},
```