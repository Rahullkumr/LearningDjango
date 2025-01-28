# Day10: 28-Jan-2025

## Folder structure of a django project


```diff
+ If you want to make any folder, a Python package, just create a "__init__.py" file inside it.
```

```python
DjangoYoutube/              # Outer project folder (root directory)
├── manage.py               # Entry point for running commands like runserver, migrate
├── DjangoYoutube/          # Inner project folder (contains settings and configurations)
│   ├── __init__.py         # Makes the 'DjangoYoutube' directory as a Python package
│   ├── asgi.py             # ASGI (Asynchronous server Gateway Interface) configuration for asynchronous deployment
│   ├── settings.py         # Main settings file for the project
│   ├── urls.py             # Root URL configuration (contains urls of every app)
│   ├── wsgi.py             # WSGI (Web Server Gateway Interface) configuration for synchronous deployment
├── app_name/               # Example app directory (replace with your app name)
│   ├── migrations/         # Stores migration files
│   │   ├── __init__.py     # Marks the directory as a Python package
│   ├── __init__.py         # Marks the directory as a Python package
│   ├── admin.py            # Admin panel configuration for the app
│   ├── apps.py             # App-specific configuration
│   ├── models.py           # Defines the database models
│   ├── tests.py            # Tests for the app
│   ├── views.py            # Handles request and response logic
├── db.sqlite3              # Default SQLite database file (if using SQLite)
├── static/                 # Folder for static files (CSS, JS, images)
│   └── ...                 # Static files go here
├── templates/              # Folder for HTML templates
│   └── ...                 # Template files go here
```

### `wsgi.py` vs `asgi.py`

- WSGI (Web Server Gateway Interface)
    - a standard interface between web server and python application which supports only synchronous web frameworks (before Django 3.1).
    - Use Cases: Simple web apps with HTTP requests/responses.
    - Limitation: Cannot handle async tasks like WebSockets or HTTP2.

- ASGI (Asynchronous Server Gateway Interface)
    - It is also a standard interface between web server and python application but it supports both synchronous and asynchronous functionality (introduced in Django 3.1)
    - Use Cases: Real-time apps (e.g., chat apps, WebSockets, HTTP2).
    - Advantage: Handles both HTTP and async protocols concurrently.


## Run Django project on specific PORT

- Run on default port i.e 8000

    ```
    python manage.py runserver
    ```

- Run on specific port (say 4000)

    ```
    python manage.py runserver 4000
    ```

## Steps to create an app (helloworld) in this project

- first activate virtual environment

- run the following command to create an app

```python
    python manage.py startapp helloworld
```
- go to settings.py and add the newly created app to installed apps list.

- create a view using views.py file which is present in the app(helloworld) folder

- goto urls.py file, add the route of that view file

- `run` the project.

- now hit that route as request in the browser and see the output.
