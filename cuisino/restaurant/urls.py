from django.urls import path, re_path
from django.conf.urls import url
import restaurant.views as views

app_name = 'restaurant'


urlpatterns=[
    path('', views.index, name="menu"),
    path('register/', views.register, name="register"),
    path('<int:id>/', views.menuitem, name="menuitem"),
    path('<int:id>/delete/', views.delete, name="delete"),
]
