from django.contrib import admin
from restaurant.models import MenuItems, Order, OrderDetails, Reservation, Table, Address

# Register your models here.
admin.site.register(MenuItems)
admin.site.register(Order)
admin.site.register(OrderDetails)
admin.site.register(Reservation)
admin.site.register(Table)
admin.site.register(Address)