# Employee Management System

A beginner-friendly Django application for viewing employee records, exploring Django Admin, and learning how models, migrations, URLs, views, templates, and a database work together. It uses Django's built-in ORM and templates; Django REST Framework is not included.

## Requirements

- Python 3.12 or newer
- PostgreSQL for the PostgreSQL configuration, or use SQLite for a quick local start

## Setup on Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Edit `.env` and set `DJANGO_SECRET_KEY` and the PostgreSQL credentials. Create a PostgreSQL database named `employee_management` and make sure the PostgreSQL service is running. To start without installing PostgreSQL, set `DATABASE_ENGINE=sqlite` in `.env`; the local SQLite database is created automatically.

## Migrate and load sample employees

```powershell
python manage.py check --database default
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata sample_employees
python manage.py createsuperuser
python manage.py runserver
```

Open `http://127.0.0.1:8000/employees/` for the directory, `/employees/1/` for an employee detail page, and `/admin/` to manage records. Sample data is safe to load on an empty database; do not load the fixture again after creating employees with the same primary keys.

## What migrations do

`makemigrations` compares model definitions with Django's migration history and writes Python migration files describing schema changes. `migrate` applies those operations to the configured database and records which migrations have run. The generated migration is checked into version control; the database file and `.env` credentials are not.

## Django request flow

`Browser -> URL pattern -> view -> Employee model/ORM -> database -> template -> browser`

The list and detail views query `Employee`, then pass model objects to Django templates for rendering. Django Admin uses the same model and ORM.

## Tests

```powershell
python manage.py test employees
```

## Git and GitHub

```powershell
git init
git add .
git commit -m "Build employee management system"
git branch -M main
git remote add origin <your-github-repository-url>
git push -u origin main
```

Create an empty GitHub repository first and replace the remote placeholder. Never commit `.env`; share `.env.example` instead.