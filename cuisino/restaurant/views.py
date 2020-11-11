from django.shortcuts import render
from restaurant.models import MenuItems

# Create your views here.
def index(request):
    menu = MenuItems.objects.all()
    options = {
        "menu": menu
    }
    return render(request, 'restaurant/index.html', options)