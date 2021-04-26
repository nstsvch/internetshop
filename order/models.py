from django.db import models
from django.contrib.auth.models import User

from main.models import Product


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return self.user.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='customer',
                                 on_delete=models.CASCADE, verbose_name='Покупатель')
    products = models.ManyToManyField(Product, verbose_name='Товары', blank=True, through='ProductInOrder')
    created = models.DateTimeField(auto_now_add=True, blank=True, verbose_name='Дата создания заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.customer} - {self.created}'


class ProductInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Товар', related_name='count_in_order',)
    quantity = models.PositiveSmallIntegerField(verbose_name='Количество товара в заказе')
