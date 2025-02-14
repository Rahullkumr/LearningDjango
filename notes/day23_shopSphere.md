# Day23: 12-Feb-2025

> new project in classProject i.e `ShopSphere`

## Folder structure

```
ShopSphere/  
│── myvenv/                        # Virtual environment  
│  
│── myproject/                     # Main project folder  
│   │── base/                      # app name  
│   │   ├── templates/             # templates folder  
│   │   │   ├── temp_base/         # child templates folder
│   │   │   │   ├── home.html  
│   │   │   │   ├── about.html  
│   │   │   ├── main.html          # parent template which has common code (boiler plate code)  
│   │   │   ├── navbar.html        # Navbar code  
│  
│   │── myproject/                 # configuration and settings folder  
│   │   ├── __init__.py            # makes this folder a py package
│   │   ├── settings.py            # Project settings  
│   │   ├── urls.py                # Project-level URLs  
│   │   ├── wsgi.py                # WSGI entry point  
│   │   ├── asgi.py                # ASGI entry point  
│  
│   │── manage.py                  # Django management script  
```