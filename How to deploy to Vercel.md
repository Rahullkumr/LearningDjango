# Django deployment - Django + Vercel + Neon DB

> A basic Django project (referring to **`dj-deploy`** repository) with a Employee model (name, mobile), deployed on **Vercel** with **Neon PostgreSQL** integration.

[![Live Demo](https://img.shields.io/badge/Website-Click_here-brightgreen)](https://dj-deploy-green.vercel.app/)

```diff
- The name of configuration folder must be `api` 
```

## 🤔 Why I Built This

- I created this project to learn how to:

    - Deploy Django apps using **Vercel**
    - Connect to serverless databases like **Neon**
    - Work with environment variables and manage secrets
    - Use **WhiteNoise** for serving static files in production


## ⚙️ Features

- Django-based web app
- PostgreSQL via [Neon](https://neon.tech/)
- Deployed on [Vercel](https://vercel.com/)
- Static files served via WhiteNoise

## 🧱 Tech Stack

- Django 5.x
- PostgreSQL (Neon)
- Vercel (Serverless deployment)
- Python-dotenv (env management)
- WhiteNoise (static files)

## 🔄 Forking the repository

- Click the **Fork** button on the top-right corner of this repo to create your own copy.


## ☁️ Deployment (Vercel)

- ### Connect GitHub Repo to Vercel  

- ### Project selection
    - Select this project from the given list and click the `Deploy` button.
    - Once deployment is complete, click the provided URL to view the live website.

## 🛢️ Neon DB Integration

1. Go to your project on [Vercel Dashboard](https://vercel.com/dashboard).

2. In the **Storage** tab, click **Connect Database** and select **Neon**.

3. Choose your database configuration and proceed.

4. Vercel will automatically provision a Neon PostgreSQL instance and set related environment variables.

5. Navigate to your project’s **Settings** → **Environment Variables**, and add a new variable:
   - **Name**: `SECRET_KEY`
   - **Value**: Your Django project's secret key

6. Go back to your forked repository.

7. Push a small change (e.g., update the README) to trigger automatic redeployment on Vercel.


You're now successfully connected to Neon PostgreSQL! 🟢

## 🙋‍♂️ Author

**Rahul Kumar**  
[@Rahullkumr](https://github.com/Rahullkumr)