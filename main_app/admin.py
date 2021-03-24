from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import ProductCategory, Product, Contacts, Images, Reviews

admin.site.register(ProductCategory)
# admin.site.register(Images)
admin.site.register(Contacts)
# admin.site.register(Reviews)


class ProductImagesInline(admin.TabularInline):
    """Изображение товара"""
    model = Images
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.upload.url}" width="100" height="auto"')

    get_image.short_description = 'Изображение'


class ReviewInlines(admin.TabularInline):
    model = Reviews
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Администрирование товаров"""
    list_display = ('category', 'name', 'price', 'quantity', 'is_active')
    list_display_links = ('category', 'name')
    inlines = [ProductImagesInline, ReviewInlines]
    save_on_top = True


