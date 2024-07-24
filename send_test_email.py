import os
import django
from django.core.mail import send_mail
from django.conf import settings

# Установите переменную окружения для настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Запустите Django
django.setup()

# Отправьте тестовое письмо
send_mail(
    'Test Subject',
    'Test Body',
    settings.DEFAULT_FROM_EMAIL,
    ['SkyStoreClub@yandex.ru'],  # Замените на тестовый адрес
    fail_silently=False,
)