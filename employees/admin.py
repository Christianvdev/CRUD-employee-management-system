from django.contrib import admin
from .models import Employee
from .models import Department
from .models import Attendance
from .models import Performance

# Register your models here.
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Attendance)
admin.site.register(Performance)