from django.urls import path

from .views import ProductListView, IndexTemplateView, ProductDetailView, CategoriesTemplateView, ContactsTemplateView, \
    AddReviewView

app_name = 'main_app'

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index'),
    path('category/', CategoriesTemplateView.as_view(), name='categories'),
    path('category/<int:pk>/', ProductListView.as_view(), name='category_products'),
    path('category/<int:pk>/page/<int:page>/', ProductListView.as_view(), name='page'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('review/<int:pk>/', AddReviewView.as_view(), name='add_review'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
]

