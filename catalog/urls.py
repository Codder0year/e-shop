from django.urls import path
from .views import contacts, HomeView, CategoriesListView, category_detail, ProductDetailView, success_page

app_name = 'catalog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('categories/', CategoriesListView.as_view(), name='categories_list'),
    path('contacts/', contacts, name='contacts'),
    path('success/', success_page, name='contacts_success'),
    path('categories/<int:pk>/', category_detail, name='category_detail'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]