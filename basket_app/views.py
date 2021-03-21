from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import F
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView
from django.views.generic.base import View

from basket_app.models import Basket
from main_app.models import Product


class BasketTemplateView(TemplateView):
    """Корзина пользователя"""
    template_name = 'basket_app/basket.html'


class BasketAddView(LoginRequiredMixin, View):
    """Добавление товара в корзину"""

    login_url = reverse_lazy('auth_app:signin')

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        basket = Basket.objects.filter(user=request.user, product=product).first()
        if basket:
            basket.quantity = F('quantity') + 1
            basket.save()
        else:
            Basket.objects.create(user=request.user, product=product, quantity=1)

        return redirect(reverse('main_app:product', args=[pk]))


class BasketDeleteView(LoginRequiredMixin, View):
    """Удаление товара из корзины"""

    login_url = reverse_lazy('auth_app:signin')

    def get(self, request, pk):
        basket_record = get_object_or_404(Basket, pk=pk)
        basket_record.delete()
        return redirect(request.META.get('HTTP_REFERER'))


class BasketEditView(View):
    """Редактирование количества товаров в корзине"""

    def get(self, request, pk, quantity):
        if request.is_ajax():
            quantity = int(quantity)
            basket_item = Basket.objects.get(pk=pk)

            if quantity > 0:
                basket_item.quantity = quantity
                basket_item.save()
            else:
                basket_item.delete()

        basket = Basket.objects.filter(user=request.user)

        result = render_to_string('includes/inc_basket_items.html', {'basket': basket})

        return JsonResponse({'result': result})
