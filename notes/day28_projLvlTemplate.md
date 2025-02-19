# Day 28: 18 Feb 2025

> project level templates and static 

## see below

- project level template
    - to keep common html code
    
- create 'templates' with configuration folder and then register the folder in settings.py so that Django knows that.

- settings > templates >

    ```py
    'DIRS': [BASE_DIR / 'templates'],
    ```

- delete all main.html files and create a main.html in project level templates 

- delete child template's folder and move the child htmls into app level > templates

- sir ka apps: fresh, electronics and base

- for static file

    ```py
    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/5.1/howto/static-files/

    STATIC_URL = 'static/'

    STATICFILES_DIRS = [
        BASE_DIR / 'static'
    ]

    # Default primary key field type
    ```