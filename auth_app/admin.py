from django.contrib import admin

from auth_app.models import ShopUser, ShopUserProfile


# admin.site.register(ShopUserProfile)


class UserProfileInlines(admin.StackedInline):
    """Отображение профиля пользователя"""
    model = ShopUserProfile


@admin.register(ShopUser)
class ShopUserAdmin(admin.ModelAdmin):
    """Администрирование пользователя"""
    list_display = ('username', 'email', 'date_joined', 'is_staff', 'is_active')
    inlines = [UserProfileInlines]
    save_on_top = True

