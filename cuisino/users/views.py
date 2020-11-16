from django.shortcuts import render
from users.forms import UserForm, EmployeeApplyForm

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


# """
#     This function adds a user as a customer.
# """
#
#
# def register(request):
#     return render(request, 'users/register.html')


"""
    This function adds a user as an employee. Can either be a chef or a delivery guy.
"""
def apply(request):
    return render(request, 'users/register.html')

@login_required
def special(request):
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return HttpResponseRedirect(reverse('home'))

def register(request):

    registered = False

    if request.method == 'POST':

        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)

        # Check to see forms are valid
        if user_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
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
        # First get the username and password supplied
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django's built-in authentication function:
        user = authenticate(username=username, password=password)

        # If we have a user
        if user:
            #Check it the account is active
            if user.is_active:
                # Log the user in.
                login(request,user)
                # Send the user back to some page.
                # In this case their homepage.
                return HttpResponseRedirect(reverse('home'))
            else:
                # If account is not active:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        #Nothing has been provided for username or password.
        return render(request, 'users/login.html', {})