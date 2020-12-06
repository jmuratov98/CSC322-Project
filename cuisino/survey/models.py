from django.db import models
from users.models import Employees, Customers

class Survey (models.Model):
    employeesCompliment = Employees.compliment
    employeesComplain = Employees.complain
    customersCompliment = Customers.compliment
    customersComplain = Customers.complain

