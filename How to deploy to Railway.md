# Django Deployment Guide - Django + Railway + PostgreSQL

This guide walks you through deploying a Django application using Railway with PostgreSQL database.

## Prerequisites

- Python installed on your system
- Git installed
- uv package manager (or pip as alternative)
- GitHub account
- Railway account

## Step 1: Setup GitHub Repository

1. Create a new GitHub repository with README and .gitignore files
2. Clone the repository to your local machine
3. Navigate into the cloned directory

```bash
git clone <your-repo-url>
cd <your-repo-name>
```

## Step 2: Create Virtual Environment

Create and activate a virtual environment:

```bash
# Create virtual environment
uv venv

# Activate virtual environment (Windows)
.venv\Scripts\activate

# Activate virtual environment (macOS/Linux)
source .venv/bin/activate
```

## Step 3: Install Dependencies

Create a `requirements.txt` file with the following dependencies:

```txt
asgiref==3.8.1
django==5.2.3
gunicorn==23.0.0
packaging==25.0
psycopg2==2.9.10
sqlparse==0.5.3
tzdata==2025.2
whitenoise==6.9.0
```

Install the packages:

```bash
uv pip install -r requirements.txt
```

## Step 4: Configure Railway Deployment

Create a `railway.json` file in the root directory:

```json
{
    "$schema": "https://railway.app/railway.schema.json",
    "build": {
        "builder": "RAILPACK"
    },
    "deploy": {
        "startCommand": "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn mysite.wsgi"
    }
}
```

## Step 5: Create Django Project

Create a new Django project:

```bash
django-admin startproject mysite .
```

Test the development server:

```bash
python manage.py runserver
```

## Step 6: Configure Django Settings

Modify `mysite/settings.py` with the following changes:

```python
import os

# Allow all hosts for deployment
ALLOWED_HOSTS = ["*"]

# Add WhiteNoise middleware for static files
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Add this line
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configure PostgreSQL database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['PGDATABASE'],
        'USER': os.environ['PGUSER'],
        'PASSWORD': os.environ['PGPASSWORD'],
        'HOST': os.environ['PGHOST'],
        'PORT': os.environ['PGPORT'],
    }
}

# Static files configuration
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
```

## Step 7: Deploy to GitHub

Commit and push your changes to GitHub:

```bash
git add .
git commit -m "Initial Django setup for Railway deployment"
git push origin main
```

## Step 8: Deploy on Railway

### Create Railway Project

1. Go to [Railway](https://railway.app) and create an account
2. Connect your GitHub account
3. Select "New Project" and choose your GitHub repository
4. Railway will automatically detect and deploy your Django application

### Add PostgreSQL Database

1. In your Railway project dashboard, right-click and select **"Add Service"**
2. Select **"PostgreSQL"** from the available services
3. Wait for the PostgreSQL service to be provisioned

### Configure Environment Variables

1. Click on your Django application 
2. Go to the **"Variables"** tab
3. Add the following environment variables:

| Variable | Value |
|----------|-------|
| `PGDATABASE` | `railway` |
| `PGHOST` | `postgres.railway.internal` |
| `PGPASSWORD` | *(Copy from PostgreSQL service variables)* |
| `PGPORT` | `5432` |
| `PGUSER` | `postgres` |
| `PORT` | `8000` |

**Note:** To get the `PGPASSWORD`, click on your PostgreSQL service and copy the password from its variables section.

## Now click on the deploy / apply changes button

- It will redeploy your project

## Step 9: Generate Domain

1. Click on your Django application 
2. Go to **"Settings"**
3. Click **"Generate Domain"**
4. Railway will provide you with a public URL

## Step 10: Access Your Application

Click on the generated domain link to access your deployed Django application!

## Resources

- [Railway Documentation](https://docs.railway.app/)
- [Django Documentation](https://docs.djangoproject.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

---

**Happy Deploying! 🚀**