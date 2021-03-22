from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Order, OrderItem

# admin.site.register(OrderItem)


class OrderItemInlines(admin.TabularInline):
    """Отображение товаров в заказе"""
    model = OrderItem
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.product.images_set.first().upload.url}" width="100" height="auto"')

    get_image.short_description = 'Изображение'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Администрирование заказов"""
    list_display = ('id', 'created', 'status', 'is_active')
    list_display_links = ('id', 'created', 'status')
    readonly_fields = ('created', 'user')
    save_on_top = True
    inlines = [OrderItemInlines]
    fieldsets = (
        (None, {
            'fields': (('status', 'is_active'),),
        }),
        (None, {
            'fields': (('created', 'user'),),
        }),
    )
