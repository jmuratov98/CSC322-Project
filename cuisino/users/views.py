from django.shortcuts import render, redirect
from users.forms import UserForm, EmployeeApplyForm
from better_profanity import profanity
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from users.models import Users


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

        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            #user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            registered = True

        else:
            print(form.errors)

    else:
        form = UserForm()

    return render(request,'users/register.html',
                           { 'form': form, 'registered': registered })

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
                if user.is_auth_by_manager or user.role == user.ADMIN:
                    login(request,user)
                    return redirect('../')
                else:
                    return redirect('/') 
            else:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'users/login.html', {})

@login_required
def dashboard(request):
    unathenticated_users = Users.objects.filter(is_auth_by_manager=False)
    print(unathenticated_users)
    return render(request, 'admin/dashboard.html', { 'users': unathenticated_users })

@login_required
def dashboard_auth(request, id):
    user = Users.objects.get(id=id)
    user.is_auth_by_manager = True
    user.save()
    return redirect("/dashboard/")

@login_required
def dashboard_delete(request, id):
    Users.objects.filter(id=id).delete()
    return redirect("/dashboard/")

def taboo_censor(request):
    if __name__ == "__main__":
        profanity.load_censor_words()

        # text = #Once Blog Implemented, string of text that gets submitted will be scanned here
        text = ''

        text = profanity.censor(text)       




def taboo_checker(request):
    count = 0
    item = Users.objects.get(warnings)
    if __name__ == "__main__":
        # text = #Once Blog Implemented, string of text that gets submitted will be scanned here
        text = ''

        if profanity.contains_profanity(text) == True:
            item.warnings += 1
            VIP_to_Reg()
            Reg_to_Rip()
            
def VIP_to_Reg():
    item = Users.objects.get(warnings,VIP)
    if item.VIP == True and item.warnings == 2:
        item.VIP = False
        item.warnings = 0


def Reg_to_Rip(id):
    item = Users.objects.get(VIP,id,warnings)
    if item.VIP == False and item.warnings == 3:
        Users.objects.filter(id=id).delete()
        return redirect ('logout/')
    