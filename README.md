# Employee Management System API

A CRUD-based REST API for managing employee data, built with Django and PostgreSQL. 
Built during my backend internship to demonstrate real-world API design with 
authentication, documentation, and relational data modeling.

## What It Does

Provides API endpoints for managing four related resources:
- **Employees** — core personnel records
- **Departments** — organizational units employees belong to
- **Attendance** — tracking employee presence over time
- **Performance** — storing performance review data per employee

## Features

- Token authentication (DRF) to secure all endpoints
- Swagger UI for interactive API documentation and testing
- PostgreSQL database with proper relational schema
- Faker integration for generating realistic test data

## Tech Stack

Python · Django · Django REST Framework · PostgreSQL · Swagger (drf-yasg)

## Installation

**Prerequisites:** Python 3.8+, PostgreSQL, Git

```bash
git clone https://github.com/Christianvdev/CRUD-employee-management-system
cd CRUD-employee-management-system
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Environment Setup

Create a `.env` file in the project root:
