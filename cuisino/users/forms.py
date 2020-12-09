from django import forms
from django.contrib.auth.models import AbstractUser
from users.models import Users
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    deposit = forms.DecimalField()

    class Meta():
        model = Users
        fields = ('username','email','password','deposit')

class EmployeeApplyForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(help_text='A valid email address, please.')
    role = forms.ChoiceField(choices=((2, 'Chef'), (3, 'Delivery')))

    class Meta():
        model = Users
        fields = ('username', 'email', 'password', 'role')
