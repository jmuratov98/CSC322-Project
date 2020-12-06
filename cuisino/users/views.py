from django.shortcuts import render
from users.forms import UserForm, EmployeeApplyForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

"""
    This function links to homepage
"""
def index(request):
    return render(request,'users/index.html')

"""
    This function adds a user as an employee. Can either be a chef or a delivery guy.
"""
def apply(request):
    return render(request, 'users/register.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def register(request):

    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True

        else:
            print(user_form.errors)

    else:
        user_form = UserForm()

    return render(request,'users/register.html',
                          {'user_form':user_form,
                           'registered':registered})

def apply(request):
    registered = False

    if request.method == 'POST':
        form = EmployeeApplyForm(data=request.POST)
        if form.is_valid():
            employee = form.save()
            employee.set_password(employee.password)
            employee = form.save()
            registered = True
        else:
            print(user_form.errors)

    elif request.method == 'GET':
        form = EmployeeApplyForm()

    return render(request, 'users/apply.html', { 'form': form, 'registered': registered })

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'users/login.html', {})
