from django.conf import settings
from django.db import models

from main_app.models import Product


class Basket(models.Model):
    """Модель представления товара в корзине"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField('Количество', default=0)
    add_datetime = models.DateTimeField('Время добавления', auto_now_add=True)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'{self.user} - {self.product} - {self.quantity}'

    def product_costs(self):
        return self.product.price * self.quantity

    def total_quantity(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum([basket.quantity for basket in baskets])

    def total_costs(self):
        baskets = Basket.objects.filter(user=self.user)
        return sum([basket.product_costs() for basket in baskets])
