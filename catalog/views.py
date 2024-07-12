from django.shortcuts import render

from catalog.models import Category


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


