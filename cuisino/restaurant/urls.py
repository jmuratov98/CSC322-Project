from django.urls import path, re_path
from django.conf.urls import url
import restaurant.views as views

app_name = 'restaurant'


urlpatterns=[
    path('', views.index, name="menu"),
    path('register/', views.register, name="register"),
    path('<int:id>/', views.menuitem, name="menuitem"),
    path('<int:id>/delete/', views.delete, name="delete"),

    path('cart/', views.cart, name="cart"),
    path('cart/add/<int:itemID>/<int:quantity>', views.add_to_cart, name="add-to-cart"),
    path('cart/remove/<int:itemID>', views.remove_from_cart, name="remove-from-cart"),

    path('search/', views.SearchResultsView, name='search_results'),
]
