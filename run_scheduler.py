import os
import django
from django.core.management import execute_from_command_line


def main():
    # Установите переменную окружения для настроек Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

    # Запустите Django
    django.setup()

    # Импортируйте задачи планировщика после настройки Django
    from mailsender import tasks

    # Запустите задачи планировщика
    tasks.start_scheduler()


if __name__ == '__main__':
    main()