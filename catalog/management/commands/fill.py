from django.core.management.base import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category_list = [
            {"1110": "1"},
            {"2": "2"},
            {"3": "3"},
            {"4": "4"},
        ]

        categories_in_create = []
        for category_item in Category_list:
            categories_in_create.append(Category(**category_item))

        Category.objects.bulk_create(categories_in_create)