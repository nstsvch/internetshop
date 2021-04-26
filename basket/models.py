from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

from main.models import Product


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="basket")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="Количество", default=0)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'{self.pk} - {self.customer.name}'
