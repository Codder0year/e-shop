from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='test@test.com',
            first_name='test',
            last_name='test',
            is_staff=True,
            is_superuser=True,

        )
        user.set_password('test')
        user.save()
