from django.shortcuts import render


def home(request):
    # функция принимает параметр request
    # и с помощью специальной функции возвращает ответ
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
