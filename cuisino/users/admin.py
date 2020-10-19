from django.contrib import admin
from users.models import Roles, Users

# Register your models here.
admin.site.register(Roles)
admin.site.register(Users)