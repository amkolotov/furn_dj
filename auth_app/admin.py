from django.contrib import admin

from auth_app.models import ShopUser, ShopUserProfile

admin.site.register(ShopUser)
admin.site.register(ShopUserProfile)

