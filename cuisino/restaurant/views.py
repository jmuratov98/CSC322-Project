from django.shortcuts import render, redirect
from restaurant.models import MenuItems, Order, OrderDetails
from restaurant.forms import MenuForm, OrderForm, ReservationForm, AddressForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

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
        form = MenuForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            menuitem = form.save()
            menuitem.save()
            registered_menuitem = True

        else:
            print(menu_form.errors)

    else:
        form = MenuForm()
    return render(request,'restaurant/item.html',
                          {'form':form,
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

    return render(request, 'restaurant/item.html', { 'form': menu_form, 'registered_menuitem': registered_menuitem, 'id': id, 'edit': True, 'orderedItem': orderedItem })

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
    order = Order.objects.get_or_create(id=request.user, ordered=False)[0]
    menuitem = MenuItems.objects.get(itemID=itemID)
    if order.items.filter(itemID=itemID).exists():
        order.items.filter(itemID=itemID).update(itemQuantity=quantity)
    else:
        item = OrderDetails.objects.create(itemID=menuitem, itemQuantity=quantity, amount=menuitem.itemPrice)
        order.items.add(item)
    return redirect('/menu/cart')

@login_required
def remove_from_cart(request, itemID):
    OrderDetails.objects.filter(itemID=itemID).delete()
    return redirect('/menu/cart')

def SearchResultsView(request):
    if 'q' in request.GET and request.GET['q']:
        # query = self.request.GET.get('q')
        q = request.GET['q']
        menu_list = MenuItems.objects.filter(
        Q(itemKeyword__icontains=q) | Q(itemDescription__icontains=q) | Q(itemName__icontains=q)
        )
        return render(request, 'restaurant/search_results.html',{'menu_list':menu_list, 'a': q})

    else:
        return render(request, 'restaurant/search_results.html')

@login_required
def complete_order(request):
    order = Order(id=request.user, ordered=False)
    purchased = False
    order_form_submitted = False

    if request.method == 'POST':
        if not order_form_submitted:
            print(request.POST)
            form = OrderForm(request.POST, instance=order)
            if form.is_valid():
                order = form.save()
                order.save()
                order_form_submitted = True
            order.refresh_from_db()
        else:
            if order.orderType == order.RESERVATION:
                form = ReservationForm(request.POST)
                if form.is_valid():
                    reservation = form.save()
                    reservation.save()
                    order.reservationID = reservation
                    order.save()
            elif order.orderType == order.DELIVERY:
                form = AddressForm(request.POST)
                if form.is_valid():
                    address = form.save()
                    address.save()
                    order.address = address
                    order.save()
            order.ordered = True
            order.save()
    else:
        if not order_form_submitted:
            form = OrderForm()
        else:
            if order.orderType == order.PICK_UP or order.orderType == order.UNKNOWN:
                return redirect('/menu/invoice')
            form = ReservationForm() if order.orderType == order.RESERVATION else AddressForm()

    options = {
        'form': form,
        "purchased": purchased

    }
    return render(request, 'restaurant/complete-order.html', options)