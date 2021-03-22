from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.db.models import F
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.base import View

from basket_app.models import Basket
from .models import OrderItem, Order


class OrderCreateView(LoginRequiredMixin, View):
    """Создание заказа пользоваьеля"""

    login_url = reverse_lazy('auth_app:signin')

    @transaction.atomic
    def get(self, request):
        baskets = Basket.objects.filter(user=request.user)
        if baskets:
            order = Order.objects.create(user=request.user)
            order.save()
            for basket in baskets:
                item = OrderItem.objects.create(order=order, product=basket.product, quantity=basket.quantity)
                item.save()
                basket.product.quantity = F('quantity') - basket.quantity
                basket.product.save()
                basket.delete()

        return render(request, 'order_app/success.html')


@receiver(pre_delete, sender=OrderItem)
def product_quantity_order_delete(sender, instance, **kwargs):
    instance.product.quantity = F('quantity') + instance.quantity
    instance.product.save()
