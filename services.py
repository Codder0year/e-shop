from django.conf import settings
from django.core.cache import cache
from catalog.models import Product


def get_cached_product_details(product_pk):
    if settings.CACHE_ENABLED:  # Проверяем, включено ли кэширование
        key = f'product_detail_{product_pk}'
        product = cache.get(key)
        if product is None:
            product = Product.objects.get(pk=product_pk)
            cache.set(key, product, timeout=60 * 15)  # Кэшируем данные на 15 минут
    else:
        product = Product.objects.get(pk=product_pk)
    return product
