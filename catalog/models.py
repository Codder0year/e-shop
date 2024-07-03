from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование', help_text='Выберите категорию')
    description = models.TextField(max_length=1000, verbose_name='описание')

    def __str__(self):
        return f'self.name, self.description'

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name = "Category"


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование', help_text='Введите азвание')
    description = models.TextField(max_length=1000, verbose_name='описание')
    image = models.ImageField(upload_to='images', verbose_name='изображение')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, verbose_name='категория', null=True, blank=True,
                                 help_text='Введите категорию')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата обновления')

    def __str__(self):
        return (f'self.name, self.category, self.price, self.date_created, self.date_updated, self.image, '
                f'self.description')


class Meta:
    verbose_name_plural = "Products"
    verbose_name = "Product"
