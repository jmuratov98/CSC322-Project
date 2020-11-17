from django import forms
from django.contrib.auth.models import AbstractUser
from restaurant.models import MenuItems

class MenuForm(forms.ModelForm):

    class Meta():
        model = MenuItems
        fields = ('category','itemName','itemDescription','itemPrice','itemImage',)
