from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import ProductListView, IndexTemplateView, ProductDetailView, CategoriesTemplateView, ContactsTemplateView

app_name = 'main_app'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('category/', CategoriesTemplateView.as_view(), name='categories'),
    path('category/<int:pk>', ProductListView.as_view(), name='category_products'),
    path('category/<int:pk>/page/<int:page>', ProductListView.as_view(), name='page'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
