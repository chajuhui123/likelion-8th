"""favSinger URL Configuration

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
import favApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', favApp.views.home, name="home"),
    path('detail/<int:detail_id>', favApp.views.detail, name = "detail"),
    path('add/', favApp.views.add, name = "add"),
    path('delete/<int:delete_id>', favApp.views.delete, name="delete"),
    path('change/<int:change_id>', favApp.views.change, name = "change"),
]
