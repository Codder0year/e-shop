from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from mailsender.models import Client
from services import get_cached_product_details
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

    def get_object(self, queryset=None):
        product_pk = self.kwargs.get('pk')
        return get_cached_product_details(product_pk)


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
        # Определяем, заблокировано ли поле `name`
        form = self.get_form()
        context['is_name_field_disabled'] = form.fields['name'].widget.attrs.get('disabled', False)
        return context


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('catalog:categories_list')

    def dispatch(self, request, *args, **kwargs):
        product = self.get_object()

        # Проверка на владельца или наличие права редактирования любых продуктов
        if product.owner != request.user and not request.user.has_perm('catalog.can_edit_any_product'):
            return HttpResponseForbidden("вы не можете редактировать .")

        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Передаем текущего пользователя в форму
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Product'
        return context


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


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('catalog:categories_list')


def unpublish_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.user.has_perm('catalog.can_unpublish_product'):
        product.is_published = False
        product.save()
        return redirect('catalog:product_detail', pk=product.id)
    else:
        return HttpResponseForbidden("У вас нет прав для отмены публикации этого продукта.")