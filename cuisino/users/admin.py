from django.contrib import admin
from users.models import Users, Employees, Customers

# Register your models here.
admin.site.register(Users)
admin.site.register(Employees)
admin.site.register(Customers)