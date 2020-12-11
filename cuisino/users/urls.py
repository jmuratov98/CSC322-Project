from django.conf.urls import url
from django.urls import path

from users import views

app_name = 'users'


urlpatterns=[
    path('', views.index, name="index"),

    path('register/', views.register, name='register'),
    path('apply/', views.apply, name='apply'),

    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
]
