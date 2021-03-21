from django.urls import path

from .views import BasketTemplateView, BasketAddView, BasketDeleteView, BasketEditView

app_name = 'basket_app'

urlpatterns = [
    path('', BasketTemplateView.as_view(), name='basket'),
    path('add/<int:pk>/', BasketAddView.as_view(), name='add'),
    path('delete/<int:pk>/', BasketDeleteView.as_view(), name='delete'),
    path('edit/<int:pk>/<int:quantity>/', BasketEditView.as_view(), name='edit'),
]
