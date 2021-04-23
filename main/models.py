from django.contrib.auth.models import User
from django.db import models
from django.db.migrations.recorder import MigrationRecorder


class ProductCategory(models.Model):
    title = models.CharField(verbose_name='Название категории', max_length=50, unique=True)

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'
        ordering = ['title']

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(verbose_name='Название товара', max_length=100)
    product_image = models.ImageField(verbose_name='Изображение', blank=True, null=True) #upload_to='images',
    description = models.CharField(verbose_name='Описание товара', max_length=200)
    price = models.PositiveIntegerField(verbose_name="Цена", default=0)
    category = models.ForeignKey(ProductCategory, verbose_name="Категория", on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


    def __str__(self):
        return self.name
