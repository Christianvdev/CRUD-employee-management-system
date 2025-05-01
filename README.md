#Employee Management System API

This is a CRUD-based Employee Management System built with Django and PostgreSQL.
This includes APIs for managing: employees, departments, attendance, and performance

Swagger UI has been integrated with this project for API documentation


#Features:

##CRUD operations for:

Employees
Departments
Attendance
Performance

Swagger UI for testing and documenting the API
PostgreSQL database for storing information
Token authentication
Faker implementation for generating fake data

#Installation:

##Prerequistes:

Python 3.8+
PostgreSQL
Git
pip and virtualenv

##Clone and setup:
git clone <https://github.com/Christianvdev/CRUD-employee-management-system>
cd <DjangoInternFolder>
python -m venv venv
venv\Scripts\activate

#.env setup:

in the root of your project add the following to your .env file:
DATABASE_URL=postgres://postgres:<yourpassword>@localhost:5432/employee_db

#Superuser creation & Token:

##to edit the database with ease and to create your token create a superuser. Follow the steps below:
python manage.py createsuperuser
python manage.py drf_create_token <superusername>
