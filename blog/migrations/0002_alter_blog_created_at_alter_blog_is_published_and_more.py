# Generated by Django 5.0.6 on 2024-07-17 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='is_published',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='views_count',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Количество просмотров'),
        ),
    ]