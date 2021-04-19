from django.contrib.auth.models import User
from django.db import models
from django.db.migrations.recorder import MigrationRecorder


class Product(models.Model):
    name = models.CharField(verbose_name='Название товара', max_length=100)
    product_image = models.ImageField(verbose_name='Изображение', upload_to='images', blank=True, null=True)
    description = models.CharField(verbose_name='Описание товара', max_length=200)
    price = models.PositiveIntegerField(verbose_name="Цена", default=0)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


    def __str__(self):
        return self.name
