from django.shortcuts import render
# from users.forms import UserForm,UserProfileInfoForm

# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
"""
    This function links to homepage
"""
def index(request):
    return render(request,'users/index.html')


"""
    This function links to homepage
"""
def home(request):
    return render(request,'home/home.html')


"""
    This function adds a user as a customer.
"""


def register(request):
    return render(request, 'users/register.html')


"""
    This function adds a user as an employee. Can either be a chef or a delivery guy.
"""
def apply(request):
    return render(request, 'users/register.html')
