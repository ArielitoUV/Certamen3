"""practica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from core import  views as core_view
from blog import views as blog_view

urlpatterns = [
    path('',core_view.index,name="index"),
    path('products/',core_view.products,name="products"),
    path('info/',core_view.info,name="info"),
    path('blog/',blog_view.blog,name="blog"),
    path('admin/', admin.site.urls),
]

