from django.apps import AppConfig


class MailsenderConfig(AppConfig):
    name = 'mailsender'

    def ready(self):
        from . import tasks
        tasks.start_scheduler()