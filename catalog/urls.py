from django.shortcuts import render
from django.urls import path
from catalog.apps import CatalogConfig

from catalog.views import contacts, home, categories_list, category_detail
app_name = CatalogConfig.name


urlpatterns = [
    path('', home, name='home'),
    path('categories/', categories_list, name='categories_list'),
    path('contacts/', contacts, name='contacts'),
    path('categories/<int:pk>/', category_detail, name='category_detail')
]
