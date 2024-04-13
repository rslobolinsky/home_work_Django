from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(max_length=250, verbose_name='Описание')

    def __str__(self):
        return f'{self.name} ({self.description})'

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField(max_length=250, verbose_name='Описание')
    photo = models.ImageField(upload_to='products/', verbose_name='Изображение (превью)', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания (записи в БД)')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения (записи в БД)')

    # manufactured_at = models.DateTimeField(**NULLABLE, verbose_name='Дата производства продукта')

    def __str__(self):
        return f'{self.name} ({self.description}) ({self.category}) ({self.price})'

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
