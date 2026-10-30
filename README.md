# Employee Management System API

A Django REST API for employees, departments, attendance, and performance reviews, built during my backend internship.

## Features

- CRUD endpoints for four related resources
- PostgreSQL database and Django migrations
- Swagger UI for exploring the API
- Faker-based sample data command

## Tech stack

Python · Django · Django REST Framework · PostgreSQL · drf-yasg

## Local setup

Requires Python 3.10 or newer, PostgreSQL, and Git.

```bash
git clone https://github.com/Christianvdev/CRUD-employee-management-system.git
cd CRUD-employee-management-system
python -m venv .venv
```

Activate the environment:

- Windows PowerShell: `.venv\Scripts\Activate.ps1`
- macOS/Linux: `source .venv/bin/activate`

```bash
python -m pip install -r requirements.txt
```

Create a PostgreSQL database and a role that can access it. Copy `.env.example` to `.env` in the repository root and replace the placeholders:

```dotenv
SECRET_KEY=replace-with-a-random-development-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=postgres://postgres:your-password@localhost:5432/employee_management
```

Generate a key with `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`.
Use your own database username, password, host, and database name. URL-encode special characters in the database password.

```bash
python manage.py check
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- API: http://127.0.0.1:8000/api/
- Swagger: http://127.0.0.1:8000/swagger/
- Admin: http://127.0.0.1:8000/admin/

## Authentication status

The current API viewsets do not enforce authenticated access. Installing DRF's token app alone does not protect the endpoints. Use this project locally; configure authentication and permissions before exposing employee data through a hosted deployment.

## Sample data

`python manage.py seed_data` creates sample records and **deletes existing employee, department, attendance, and performance records first**. Use it only against a disposable development database.

## Repository hygiene

Local environment files, SQLite databases, and generated Python caches are ignored. Database structure is maintained through the committed Django migrations.
