from django.urls import path
from .views import HomeView, contacts, success_page, CategoriesListView, category_detail, ProductDetailView
from .views import ProductCreateView, ProductUpdateView, ProductVersionCreateView, ProductVersionUpdateView

app_name = 'catalog'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('categories/', CategoriesListView.as_view(), name='categories_list'),
    path('contacts/', contacts, name='contacts'),
    path('success/', success_page, name='contacts_success'),
    path('categories/<int:pk>/', category_detail, name='category_detail'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('version/create/', ProductVersionCreateView.as_view(), name='version_create'),
    path('version/<int:pk>/update/', ProductVersionUpdateView.as_view(), name='version_update'),
]