from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    slug = models.CharField(max_length=200, verbose_name='Slug')
    body = models.TextField(verbose_name='Содержание')
    preview = models.ImageField(upload_to='blog_images/', verbose_name='Превью')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания', blank=True, null=True)
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано', blank=True, null=True)
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров', blank=True, null=True)

    def str(self):
        return (f'{self.title} '
                f'{self.slug} '
                f'{self.body} '
                f'{self.preview} '
                f'{self.created_at} '
                f'{self.is_published} '
                f'{self.views_count} '
                f'')

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'