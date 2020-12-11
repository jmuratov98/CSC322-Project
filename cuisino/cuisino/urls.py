"""cuisino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include

from home import views as home_views
from Blog import views as Blog_views

urlpatterns = [
    path('', home_views.index, name='home'),
    path('admin/', admin.site.urls),
    path('menu/', include('restaurant.urls')),
    path('users/',include('users.urls')),

    url(r'^blog/', include(('Blog.urls', 'blog'), namespace='blog')),
    #path('blog/', Blog_views.list_of_post),
    #path('blog/<slug:slug>/', Blog_views.post_detail, name="post_detail"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
