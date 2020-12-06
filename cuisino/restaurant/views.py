from django.shortcuts import render, redirect
from restaurant.models import MenuItems
from restaurant.forms import MenuForm
from django.urls import reverse

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

def index(request):
    menu = MenuItems.objects.all()
    options = {
        "menu_list": menu
    }
    return render(request, 'restaurant/index.html', options)

def register(request):

    registered_menuitem = False

    if request.method == 'POST':
        menu_form = MenuForm(data=request.POST, files=request.FILES)
        if menu_form.is_valid():
            menuitem = menu_form.save()
            menuitem.save()
            registered_menuitem = True

        else:
            print(menu_form.errors)

    else:
        menu_form = MenuForm()
    return render(request,'restaurant/item.html',
                          {'menu_form':menu_form,
                           'registered_menuitem':registered_menuitem,
                           'edit': False})

def menuitem(request, id):
    item = MenuItems.objects.get(itemID=id)

    registered_menuitem = False

    if request.method == 'POST':
        form = MenuForm(data=request.POST, files=request.FILES, instance=item)
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


""" Shopping Cart """
def cart(request):
    pass

def add_to_cart(request, itemID, quantity):
    pass

def remove_from_cart(request, itemID):
    pass
