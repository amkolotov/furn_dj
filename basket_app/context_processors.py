from auth_app.models import ShopUser


def basket(request):
    """Коризина пользователя"""
    basket = []
    if request.user.is_authenticated:
        basket = request.user.basket_set.all()
    return {'basket': basket}
