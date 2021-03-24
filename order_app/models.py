from django.conf import settings
from django.db import models

from main_app.models import Product


class Order(models.Model):
    """Заказ пользователя"""
    SENT = 'ST'
    ACCEPTED = 'AC'
    READY = 'RD'
    DONE = 'DN'
    CANCEL = 'CL'

    ORDER_STATUSES = (
        (SENT, 'Отправлен в обработку'),
        (ACCEPTED, 'Принят в работу'),
        (READY, 'Готов к выдаче'),
        (DONE, 'Завершен'),
        (CANCEL, 'Отменен')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    status = models.CharField('Статус', max_length=2, choices=ORDER_STATUSES, default=SENT)
    is_active = models.BooleanField('Активен', default=True, db_index=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-created',)

    def __str__(self):
        return f'Заказ {self.pk} - {self.user}'


class OrderItem(models.Model):
    """Товар в заказе"""
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заказ')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = models.PositiveIntegerField('Количество', default=0)

    class Meta:
        verbose_name = 'Товар в заказ'
        verbose_name_plural = 'Товары в заказ'

    def __str__(self):
        return self.product.name
