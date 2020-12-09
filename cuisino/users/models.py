from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext as _
from autoslug.fields import AutoSlugField  #django-autoslug package 
from ckeditor.fields import RichTextField

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

    salary = models.DecimalField(max_digits=5, decimal_places=2, default=15.00)
    demoted = models.BooleanField(default=False)

class Customers(Users):
    class Meta:
        verbose_name = 'customer'
        verbose_name_plural = 'customers'

    warnings = models.IntegerField(default=0)
    VIP = models.BooleanField(default=False)
    demoted = models.BooleanField(default=False)
    deposit = models.DecimalField(decimal_places=2, max_digits=5, default=0.00)


class Blog(models.Model):
    class Meta: 
        verbose_name = 'blog post'
        verbose_name_plural = 'blog posts'
        ordering = ['pub_date']             #date post was published

    title = models.CharField(_('title'), max_length=255)
    slug = AutoSlugField(_('slug'), populate_from='title', unique=True)
    image = models.ImageField(_('image'), blank=True, null=True, upload_to='blog')
    text = RichTextField(_('text'))
    description = models.TextField(_('description'), blank=True, null=True)
    published = models.BooleanField(_('published'), default=False)

    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    pub_date = models.DateTimeField(_('publish date'), blank=True, null=True)