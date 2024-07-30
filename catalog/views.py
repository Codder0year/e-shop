from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView

from mailsender.models import Client
from .models import Category, Product, Version
from .forms import ProductForm, ProductVersionForm


class HomeView(TemplateView):
    template_name = 'home.html'


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        # Создаем и сохраняем новый объект Client
        Client.objects.create(
            email=email,
            name=name,
            phone=phone,
            comment=message
        )

        # Перенаправляем на страницу успешной отправки
        return redirect('contacts_success')

    return render(request, 'contacts.html')


def success_page(request):
    return render(request, 'success.html')


class CategoriesListView(ListView):
    model = Category
    template_name = 'categories_list.html'
    context_object_name = 'categories'


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'category_detail.html', context=context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = '/products/'


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = '/products/'


class ProductVersionCreateView(CreateView):
    model = Version
    form_class = ProductVersionForm
    template_name = 'version_form.html'
    success_url = '/versions/'


class ProductVersionUpdateView(UpdateView):
    model = Version
    form_class = ProductVersionForm
    template_name = 'version_form.html'
    success_url = '/versions/'
