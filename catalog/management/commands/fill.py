from django.core.management.base import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Category_list = [
            {"name": "Electronics", "description": "Electronic devices and gadgets."},
            {"name": "Books", "description": "A variety of books across different genres."},
            {"name": "Clothing", "description": "Men's, women's, and children's clothing."},
        ]

        categories_in_create = []
        for category_item in Category_list:
            categories_in_create.append(Category(**category_item))

        Category.objects.bulk_create(categories_in_create)