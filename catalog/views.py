from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
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

        Client.objects.create(
            email=email,
            name=name,
            phone=phone,
            comment=message
        )
        return redirect('catalog:contacts_success')

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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:categories_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user  # Привязываем текущего пользователя к продукту
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Product'
        return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:categories_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Product'
        return context

    def get_queryset(self):
        # Пользователь может редактировать только свои продукты
        return super().get_queryset().filter(owner=self.request.user)


class ProductVersionCreateView(CreateView):
    model = Version
    form_class = ProductVersionForm
    template_name = 'version_form.html'
    success_url = reverse_lazy('catalog:categories_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create Product Version'
        return context


class ProductVersionUpdateView(UpdateView):
    model = Version
    form_class = ProductVersionForm
    template_name = 'version_form.html'
    success_url = reverse_lazy('catalog:categories_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Product Version'
        return context