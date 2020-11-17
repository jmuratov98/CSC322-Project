from django.shortcuts import render, redirect
from restaurant.models import MenuItems
from restaurant.forms import MenuForm
from django.urls import reverse

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

# from django.contrib.auth.decorators import permission_required

# Create your views here.
def index(request):
    menu = MenuItems.objects.all()
    options = {
        "menu": menu
    }
    return render(request, 'restaurant/index.html', options)

# @permission_required('MenuItems.add_item')
# def your_fuc(request):
#     or you can rise permission denied exception


def register_menuitem(request):

    registered_menuitem = False

    if request.method == 'POST':

        # It appears as one form to the user on the .html page
        menu_form = MenuForm(data=request.POST)

        # Check to see form are valid
        if menu_form.is_valid():

            # Save menuitem Form to Database
            menuitem = menu_form.save()

            menuitem.save()

            # Registration Successful!
            registered_menuitem = True

        else:
            # One of the forms was invalid if this else gets called.
            print(menu_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        menu_form = MenuForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'restaurant/item.html',
                          {'menu_form':menu_form,
                           'registered_menuitem':registered_menuitem,
                           'edit': False})

def menuitem(request, id):
    item = MenuItems.objects.get(itemID=id)

    registered_menuitem = False

    if request.method == 'POST':
        form = MenuForm(data=request.POST)
        if form.is_valid():
            menuitem = form.save()
            menuitem.save()
            registered_menuitem = True
    elif request.method == 'GET':
        form = MenuForm(initial=item)

    return render(request, 'restaurant/item.html', { 'menu_form': form, 'registered_menuitem': registered_menuitem, 'id': id, 'edit': True })

def delete(request, id):
    item = MenuItems.objects.get(itemID=id)
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    return render(request, 'restaurant/delete.html')

# """
#     This function links to Menu
# """
# def menu(request):
#     return render(request,'restaurant/menu.html')

"""
    This function links to Menu
"""
class menu(ListView):
    model = MenuItems
    context_object_name = 'menu_list'
    def get_queryset(self):
        return MenuItems.objects.order_by('itemID')

