from django.contrib.auth.models import User
from django.db import models

from main.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # или вместо User - settings.AUTH_USER_MODEL
    count = models.PositiveIntegerField(verbose_name="Количество", default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
