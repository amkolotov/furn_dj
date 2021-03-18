from django.contrib import admin

from .models import ProductCategory, Product, Contacts, Images, Reviews

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Images)
admin.site.register(Contacts)
admin.site.register(Reviews)
