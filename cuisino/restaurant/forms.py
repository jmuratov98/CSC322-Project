from django import forms
from django.contrib.auth.models import AbstractUser
from restaurant.models import MenuItems

class MenuForm(forms.ModelForm):
    category = forms.ChoiceField(choices=MenuItems.MENU_CATEGORY_CHOICES, required=True, label='Category')
    itemName = forms.CharField(max_length=50, min_length=3, required=True, label='Name')
    itemDescription = forms.CharField(widget=forms.TextInput, label='Description')
    itemPrice = forms.DecimalField(max_value=1000.00, label='Price')
    itemImage = forms.ImageField(label='Image',required=False)

    class Meta():
        model = MenuItems
        fields = ('category','itemName','itemDescription','itemPrice','itemImage')
