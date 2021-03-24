import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.base import View

from .forms import ReviewForm
from .models import Product, ProductCategory, Contacts, Reviews


def get_hot_product():
    return random.choice(Product.objects.filter(is_active=True))


def get_sample_product(product):
    return random.sample(
        list(Product.objects.filter(category=product.category, is_active=True).exclude(pk=product.id)), k=3
    )


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
        context.update({
            'sample_products': get_sample_product(context['object']),
            'form': ReviewForm()
        })
        return context


class SearchView(View):
    """Обработка поискового запроса"""

    def get(self, request):
        search = request.GET.get('search')
        if search:
            category = ProductCategory.objects.filter(name__icontains=search)
            if category:
                return redirect(reverse('main_app:category_products', args=[category.first().pk]))
            product = Product.objects.filter(name__icontains=search)
            if product:
                return redirect(reverse('main_app:product', args=[product.first().pk]))

        return redirect(reverse('main_app:category_products', args=[0]))


class AddReviewView(LoginRequiredMixin, View):
    """Добавление отзыва на товар"""
    login_url = reverse_lazy('auth_app:signin')

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        product = Product.objects.get(pk=pk)
        if form.is_valid():
            review = form.save(commit=False)
            review.product_id = pk
            review.user = request.user
            if request.POST.get('parent', None):
                review.parent_id = int(request.POST.get('parent', None))
            form.save()
        return redirect(product.get_absolute_url())


class ContactsTemplateView(TemplateView):
    """Вывод контакной информации"""
    template_name = 'main_app/contacts.html'
    extra_context = {'contacts': Contacts.objects.all()}


