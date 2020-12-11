from django.urls import path, re_path
from django.conf.urls import url
import restaurant.views as views

app_name = 'restaurant'


urlpatterns=[
    path('', views.index, name="menu"),
    path('register/', views.register, name="register"),
    path('<int:id>/', views.cartitem, name="menuitem"),
    path('<int:id>/delete/', views.delete, name="delete"),
    path('complete-order/<uuid:id>', views.complete_order, name="complete-order"),
    path('complete-order/<uuid:id>/reservation/', views.complete_order_reservation, name="complete-order-reservation"),
    path('complete-order/<uuid:id>/delivery/', views.complete_order_delivery, name="complete-order-delivery"),
    path('complete-order/<uuid:id>/pickup/', views.complete_order_pickup, name="complete-order-pickup"),
    path('invoice', views.complete_order, name="invoice"),

    path('cart/', views.cart, name="cart"),
    path('cart/add/<int:itemID>/<int:quantity>', views.add_to_cart, name="add-to-cart"),
    path('cart/remove/<int:itemID>', views.remove_from_cart, name="remove-from-cart"),

    path('search/', views.SearchResultsView, name='search_results'),
]
