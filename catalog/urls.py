from django.shortcuts import render
from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import contacts, home
from catalog.views import categories_list
app_name = CatalogConfig.name


urlpatterns = [
    path('', home, name='home'),
    path('categories/', categories_list, name='categories_list'),
    path('contacts/', contacts, name='contacts'),
]
