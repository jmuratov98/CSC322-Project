from django.urls import path
from django.conf.urls import url
import restaurant.views as views

app_name = 'restaurant'


urlpatterns=[
    path('', views.index),
    # path('/menu/add/', views.add),
    # path('/menu/edit/', views.edit),
    # path('/menu/remove/', views.remove),
    url(r'^menu/$',views.menu.as_view(),name='menu'),
    url(r'^register_menuitem/$',views.register_menuitem,name='register_menuitem'),
]
