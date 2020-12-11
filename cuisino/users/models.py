from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

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
    demoted = models.BooleanField(default=False)
    is_auth_by_manager = models.BooleanField(default=False)

    # customer
    warnings = models.IntegerField(blank=True, null=True)
    VIP = models.BooleanField(blank=True, null=True)
    deposit = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)
    # employee
    salary = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    USERNAME_FIELD = 'username'
