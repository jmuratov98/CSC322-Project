from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

from uuid import uuid4

# Create your models here.
# class Roles(models.Model):
#     # These are the different types of Roles
#     CUSTOMER = 1
#     CHEF = 2
#     DELIVERY_BOY = 3
#     ADMIN = 4 # This is going to be the owner

#     ROLE_CHOICES = [
#         ( CUSTOMER, 'Customer' ),
#         ( CHEF, 'Chef' ),
#         ( DELIVERY_BOY, 'Delivery Boy' ),
#         ( ADMIN, 'Admin' )
#     ]

#     id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

#     def __str__(self):
#         return self.get_id_display()

class Users(AbstractUser):
    CUSTOMER = 1
    CHEF = 2
    DELIVERY_BOY = 3
    ADMIN = 4 # This is going to be the owner

    ROLE_CHOICES = [
        ( CUSTOMER, 'Customer' ),
        ( CHEF, 'Chef' ),
        ( DELIVERY_BOY, 'Delivery Boy' ),
        ( ADMIN, 'Admin' )
    ]

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
    
    id = models.AutoField(primary_key=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=CUSTOMER)
    messages = models.TextField(null=True, blank=True)

    USERNAME_FIELD = 'username'

    
class Employees(Users):

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'

    salary = models.DecimalField(max_digits=5, decimal_places=2)
    demoted = models.BooleanField(default=False)

class Customers(Users):
    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    warnings = models.IntegerField()
    VIP = models.BooleanField(default=False)
    demoted = models.BooleanField(default=False)
    deposit = models.DecimalField(decimal_places=2, max_digits=5, default=0.00)
