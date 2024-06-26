# Generated by Django 5.0.4 on 2024-04-13 11:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование')),
                ('description', models.TextField(max_length=250, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Наименование')),
                ('description', models.TextField(max_length=250, verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Изображение (превью)')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания (записи в БД)')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения (записи в БД)')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
