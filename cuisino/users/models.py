from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Roles(models.Model):
    # These are the different types of Roles
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

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()

class Users(AbstractUser):
    id = models.AutoField(primary_key=True)
    role = models.ManyToManyField(Roles)

