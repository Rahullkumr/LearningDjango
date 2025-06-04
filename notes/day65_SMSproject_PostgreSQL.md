# Day 65: 14 April 2025

> Student Management System using PostgreSQL

# PostgreSQL Installation and Configuration Guide


## Step 1: Install PostgreSQL Server on Windows

1. **Download PostgreSQL** 
   - [PostgreSQL Downloads](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)

2. **Run the Installer**:
   - Run the downloaded installer.
   - During installation, **uncheck pgAdmin** (optional), **uncheck StackBuilder**, and keep **PostgreSQL Server** selected.
   - Set a **password** for the superuser `postgres` — remember this for later!
   - Keep default **port** `5432` (or change if needed).
   - Complete the installation.

3. **Verify PostgreSQL Installation**:
   - Open the **SQL Shell (psql)** from the Start menu.
   - Enter:
     - Server [`localhost`]: 
     - Database [`postgres`]: 
     - Port [`5432`]: 
     - Username [`postgres`]: 
     - Password: (the one you set during installation)
   - If connected successfully, you should see:
     ```
     postgres=#
     ```

## Step 2: Install psycopg2 (PostgreSQL Adapter)

- This is the adapter that allows Django to connect to PostgreSQL.

   ```bash
   pip install psycopg2
   ```


## Step 3: Configure PostgreSQL Database in Django

1. **Create a Database in PostgreSQL**:

   - Open the **SQL Shell (psql)** again and create a new database for your project:
     
      ```sql
      CREATE DATABASE your_db_name;
      ```

2. **Update `settings.py` in Django**:

   - In your Django project, open the `settings.py` file and configure the `DATABASES` setting like this:

      ```python
      DATABASES = {
         'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',        # The database you just created
            'USER': 'postgres',            # Default user
            'PASSWORD': 'your_password',   # Password you set during installation
            'HOST': 'localhost',
            'PORT': '5432',
         }
      }
      ```

## Step 4: Run Django Migrations

- This will apply all migrations and create the default Django tables (like `auth`, `sessions`, etc.) in your PostgreSQL database.

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## Step 5: Verify the Connection

- Run the development server

   ```bash
   python manage.py runserver
   ```

- Go to `http://127.0.0.1:8000/` in your browser. 

- If everything is set up correctly, your Django app should be running, and data will be stored in PostgreSQL.

## Conclusion

- You're now using PostgreSQL with Django!