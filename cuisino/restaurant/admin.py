from django.contrib import admin
from restaurant.models import MenuItems, Order, OrderDetails

# Register your models here.
admin.site.register(MenuItems)
admin.site.register(Order)
admin.site.register(OrderDetails)