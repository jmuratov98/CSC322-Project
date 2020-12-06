from django.db import models
from restaurant.models import MenuItems



class Star (models.Model):
    star = MenuItems.reviewStar