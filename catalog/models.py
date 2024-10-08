from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование', help_text='Выберите категорию')
    description = models.TextField(max_length=1000, verbose_name='описание')
    image = models.ImageField(upload_to='images', verbose_name='изображение', null=True, blank=True)

    def __str__(self):
        return f'{self.name}, {self.description}'

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование', help_text='Введите название')
    description = models.TextField(max_length=1000, verbose_name='описание')
    image = models.ImageField(upload_to='images', verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='категория', null=True, blank=True,
                                 help_text='Введите категорию')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')  # Новое поле для публикации

    def __str__(self):
        return (f'{self.name}, {self.category}, {self.price}, {self.created_at}, {self.updated_at}, {self.image}, '
                f'{self.description}')

    class Meta:
        verbose_name_plural = "Products"
        verbose_name = "Product"
        permissions = [
            ('can_unpublish_product', 'Может отменять публикацию продукта'),
            ('can_edit_any_product', 'Может редактировать любой продукт'),
            ('can_change_category', 'Может менять категорию любого продукта'),
        ]


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions')
    version_number = models.CharField(max_length=20)
    version_name = models.CharField(max_length=255)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.version_name} ({self.version_number})"