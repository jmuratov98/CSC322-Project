from django.shortcuts import render, redirect
from restaurant.models import MenuItems, Order, OrderDetails
from restaurant.forms import MenuForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

# Create your views here.
def index(request):
    menu = MenuItems.objects.all()
    options = {
        "menu_list": menu
    }
    return render(request, 'restaurant/index.html', options)

@login_required
def register(request):

    registered_menuitem = False

    if request.method == 'POST':

        # It appears as one form to the user on the .html page
        menu_form = MenuForm(data=request.POST, files=request.FILES)

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

@login_required
def menuitem(request, id):
    item = MenuItems.objects.get(itemID=id)
    try: 
        orderedItem = Order.objects.get(id=request.user.id, ordered=False).items.get(itemID=id)
    except:
        orderedItem = None

    registered_menuitem = False

    if request.method == 'POST':
        menu_form = MenuForm(data=request.POST, files=request.FILES, instance=item)
        if menu_form.is_valid():
            menuitem = menu_form.save()
            menuitem.save()
            registered_menuitem = True
    elif request.method == 'GET':
        menu_form = MenuForm(initial=item)

    return render(request, 'restaurant/item.html', { 'menu_form': menu_form, 'registered_menuitem': registered_menuitem, 'id': id, 'edit': True, 'orderedItem': orderedItem })

@login_required
def delete(request, id):
    item = MenuItems.objects.get(itemID=id)
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    return render(request, 'restaurant/delete.html')


""" Shopping Cart """
@login_required
def cart(request):
    try: 
        order = Order.objects.get(id=request.user.id, ordered=False)
    except:
        order = None
    return render(request, 'restaurant/cart.html', { 'order': order })

@login_required
def add_to_cart(request, itemID, quantity):
    order = Order.objects.get_or_create(id=request.user.id, ordered=False)[0]
    menuitem = MenuItems.objects.get(itemID=itemID)
    if order.items.filter(itemID=itemID).exists():
        order.items.filter(itemID=itemID).update(itemQuantity=quantity)
    else:
        item = OrderDetails.objects.create(itemID=itemID, itemQuantity=quantity, amount=menuitem.itemPrice)
        order.items.add(item)
    return redirect('/menu/cart')

@login_required
def remove_from_cart(request, itemID):
    OrderDetails.objects.filter(itemID=itemID).delete()
    return redirect('/menu/cart')
