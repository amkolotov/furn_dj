from .models import ProductCategory


def categories(request):
    """Список категорий товаров"""
    categories = ProductCategory.objects.filter(is_active=True)
    return {'categories': categories}
