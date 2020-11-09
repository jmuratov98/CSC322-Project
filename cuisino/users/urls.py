from django.conf.urls import url
from users import views

app_name = 'users'


urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^index/$',views.index,name='index'),

    # url(r'^user_login/$',views.user_login,name='user_login'),
    # url(r'^logout/$', views.user_logout, name='logout'),
]
