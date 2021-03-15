import random

from django.shortcuts import get_object_or_404
from django.views.generic import ListView, TemplateView, DetailView

from .models import Product, ProductCategory, Contacts


def get_hot_product():
    return random.choice(Product.objects.filter(is_active=True))


def get_sample_product(product):
    return random.sample(list(Product.objects.filter(category=product.category, is_active=True)), k=3)


class IndexTemplateView(TemplateView):
    """Главная страница"""
    extra_context = {'objects': random.sample(list(Product.objects.filter(is_active=True)), k=3)}
    template_name = 'main_app/index.html'


class CategoriesTemplateView(TemplateView):
    """Меню выбора категорий продуктов"""
    template_name = 'main_app/categories.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hot_product = get_hot_product()
        context.update({
            'categories': ProductCategory.objects.filter(is_active=True),
            'hot_product': hot_product,
            'sample_products': get_sample_product(hot_product)
        })
        return context


class ProductListView(ListView):
    """Вывод продуктов определенной категории"""

    paginate_by = 4

    def get_queryset(self):
        if self.kwargs['pk'] == 0:
            return Product.objects.filter(is_active=True).order_by('price')
        return Product.objects.filter(category__pk=self.kwargs['pk'], is_active=True).order_by('price')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs['pk'] == 0:
            category = {'pk': 0, 'name': 'Все'}
        else:
            category = get_object_or_404(ProductCategory, pk=self.kwargs['pk'], is_active=True)
        context.update({
            'categories': ProductCategory.objects.filter(is_active=True),
            'category': category
        })
        return context


class ProductDetailView(DetailView):
    """Вывод конкретного продукта"""
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'sample_products': get_sample_product(context['object'])})
        return context


class ContactsTemplateView(TemplateView):
    """Вывод контакной информации"""
    template_name = 'main_app/contacts.html'
    extra_context = {'contacts': Contacts.objects.all()}
