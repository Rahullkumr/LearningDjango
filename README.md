# Learning Django

Learning Django from Rajat Naroji sir

![](./Django%205.png)

## MVC architecture 
![](./MVCbysir.jpg)


## MVT architecture (used by Django)
![](./MVTbysir.png)

## Ideal Folder structure for a Django project

```
DjangoProject/              # Outer project folder (root directory)
├── manage.py               # Entry point for running commands
├── .env                    # Environment variables (not committed to Git)
├── .gitignore              # Files and folders to ignore in Git
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
├── config/                 # Configuration directory (instead of DjangoProject/)
│   ├── __init__.py        # Makes it a Python package
│   ├── asgi.py            # ASGI configuration 
│   ├── settings/          # Split settings (modular settings approach)
│   │   ├── __init__.py
│   │   ├── base.py        # Base settings
│   │   ├── dev.py         # Development settings
│   │   ├── prod.py        # Production settings
│   │   ├── local.py       # Local settings
│   ├── urls.py            # Root URL configuration
│   └── wsgi.py            # WSGI configuration
├── apps/                   # Directory for all Django apps
│   ├── __init__.py
│   ├── core/              # Core utilities and shared logic
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── serializers.py
│   │   ├── forms.py
│   │   ├── admin.py
│   │   ├── tests.py
│   │   ├── signals.py
│   │   └── tasks.py       # Celery tasks (if used)
│   ├── users/             # User management app
│   ├── products/          # Example of another app (e.g., products)
│   ├── orders/            # Orders app
├── static/                # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   └── images/
├── templates/             # Global templates
│   ├── base.html
│   ├── users/
│   ├── products/
│   └── orders/
├── media/                 # Uploaded media files (ignored in Git)
├── logs/                  # Log files
└── scripts/               # Utility scripts (e.g., database backups, automation)

```

## Reload browser automatically

- Install

```batch
pip install django-browser-reload
```

- modify settings.py

```django
INSTALLED_APPS = [
    ...existing code...
    "django_browser_reload",
    ...existing code...
]

MIDDLEWARE = [
    ...existing code...
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    ...existing code...
]
```

- add to main urls.py

```django
from django.urls import include, path

urlpatterns = [
    ...existing code...
    path("__reload__/", include("django_browser_reload.urls")),
]
```

- finally run server

```python
python manage.py runserver
```