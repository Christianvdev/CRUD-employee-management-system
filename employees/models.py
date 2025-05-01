from django.db import models
import datetime
from django.core.exceptions import ValidationError

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    date_joined = models.DateField()
    department = models.CharField(max_length=255)
    

    def __str__(self):
        return self.name
    



class Department(models.Model):
    department_name = models.CharField(max_length=255)

    def __str__(self):
        return self.department_name
    


    
class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.employee.name} - {self.status}"
    



class Performance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, default=1)
    rating = models.IntegerField()
    review_date = models.DateField(default=datetime.date.today)

    def save(self, *args, **kwargs):
        if self.rating < 1 or self.rating > 5:
            raise ValidationError("Rating must be 1-5")
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.employee.name} - Rating: {self.rating}"
