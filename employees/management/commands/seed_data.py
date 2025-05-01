from django.core.management.base import BaseCommand
from faker import Faker
import random
from employees.models import Employee, Department, Attendance, Performance

class Command(BaseCommand):
    help = 'Seed the database with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        print("Seeding data")

        # clear any existing data
        Department.objects.all().delete()
        Employee.objects.all().delete()
        Attendance.objects.all().delete()
        Performance.objects.all().delete()

        dept_names = ['Engineering', 'HR', 'Sales', 'Marketing', 'Finance']
        departments = []
        for name in dept_names:
            dept = Department.objects.create(department_name=name)
            departments.append(dept)

        employees = []
        for _ in range(50):
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                date_joined=fake.date_between(start_date='-2y', end_date='today'),
                department=random.choice(departments)
            )
            employees.append(emp)

        for emp in employees:
            for _ in range(10):
                Attendance.objects.create(
                    employee=emp,
                    date=fake.date_between(start_date='-30d', end_date='today'),
                    status=random.choice(['Present', 'Absent', 'Late'])
                )
            for _ in range(3):
                Performance.objects.create(
                    employee=emp,
                    rating=random.randint(1, 5),
                    review_date=fake.date_between(start_date='-6m', end_date='today')
                )

        print("Done seeding data.")