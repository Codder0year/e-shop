import string
import random
from django.contrib.auth.hashers import make_password
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView
from django.core.mail import send_mail
from users.forms import CustomLoginForm, CustomUserCreationForm
from users.models import User


class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = 'users/login.html'


class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'users/register.html'
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        send_mail(
            "Добро пожаловать в Skystore!",
            "Спасибо за регистрацию в Skystore.",
            "SkyStoreClub@yandex.ru",
            [self.object.email],
            fail_silently=False,
        )
        return response


class PasswordResetView(View):
    @staticmethod
    def get(request):
        return render(request, 'users/password_reset.html')

    @staticmethod
    def post(request):
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            user.password = make_password(new_password)
            user.save()
            send_mail(
                "Восстановление пароля",
                f"Ваш новый пароль: {new_password}",
                "SkyStoreClub@yandex.ru",
                [email],
                fail_silently=False,
            )
            return redirect('users:login')
        except User.DoesNotExist:
            return render(request, 'users/password_reset.html', {'error': 'Пользователь с таким адресом не найден.'})
