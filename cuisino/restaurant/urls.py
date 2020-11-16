from django.urls import path, re_path
from django.conf.urls import url
import restaurant.views as views

app_name = 'restaurant'


urlpatterns=[
    path('', views.index),
    path('<int:id>/', views.menuitem, name="menuitem"),
    path('<int:id>/delete/', views.delete, name="delete"),
    path('menu/', views.menu.as_view(), name='menu'),
    path('register_menuitem/', views.register_menuitem, name='register_menuitem'),
]
