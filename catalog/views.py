from django.shortcuts import render, get_object_or_404

from catalog.models import Category, Product


def home(request):
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        # в переменной request хранится информация о методе, который отправлял пользователь
        name = request.POST.get('name')
        message = request.POST.get('message')
        phone = request.POST.get('phone')
        # а также передается информация, которую заполнил пользователь
        print(name, message, phone)
    return render(request, 'contacts.html')


def categories_list(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'categories_list.html', context=context)


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'category_detail.html', context=context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context=context)