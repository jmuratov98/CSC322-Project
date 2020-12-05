from django import forms
from django.contrib.auth.models import AbstractUser
from users.models import Customers, Employees

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = Customers
        fields = ('username','email','password')

class EmployeeApplyForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(help_text='A valid email address, please.')
    role = forms.ChoiceField(choices=((2, 'Chef'), (3, 'Delivery')))

    class Meta():
        model = Employees
        fields = ('username', 'email', 'password', 'role')
