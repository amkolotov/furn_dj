from auth_app.models import ShopUser
from main_app.models import ProductCategory


def basket(request):
    """Корзина пользователя"""
    basket = []
    if request.user.is_authenticated:
        basket = request.user.basket_set.select_related('product')
    return {'basket': basket}
