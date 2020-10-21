from django.shortcuts import render

# Create your views here.
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