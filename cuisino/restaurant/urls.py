from django.urls import path
import restaurant.views as views

app_name = 'restaurant'


urlpatterns=[
    path('', views.index),
    # path('/menu/add/', views.add),
    # path('/menu/edit/', views.edit),
    # path('/menu/remove/', views.remove),
]
