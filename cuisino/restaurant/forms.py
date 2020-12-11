from django import forms
from django.contrib.auth.models import AbstractUser
from restaurant.models import MenuItems, Order, Address, Reservation
from users.models import Users

class MenuForm(forms.ModelForm):
    category = forms.ChoiceField(choices=MenuItems.MENU_CATEGORY_CHOICES, required=True, label='Category')
    itemName = forms.CharField(max_length=50, min_length=3, required=True, label='Name')
    itemDescription = forms.CharField(widget=forms.TextInput, label='Description')
    itemPrice = forms.DecimalField(max_value=1000.00, label='Price')
    itemImage = forms.ImageField(label='Image',required=False)

    class Meta():
        model = MenuItems
        fields = ('category','itemName','itemDescription','itemPrice','itemImage')

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ('address1', 'address2', 'city', 'state', 'zipCode')        

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('tableID', 'datetime', 'duration')

class OrderForm(forms.ModelForm):
    chef = forms.ModelChoiceField(label="Chefs", queryset=None)

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['chef'].queryset = Users.objects.filter(role=Users.CHEF)
    
    class Meta:
        model = Order
        fields = ('orderType', 'chef')