from django import forms
from django.contrib.auth.models import AbstractUser
from users.models import Users

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = Users
        fields = ('username','email','password')
