from django.db import models


def product_directory_path(instance, filename):
    return f'product_images/{instance.product.category.name}/{instance.product.name}/{filename}'


class ProductCategory(models.Model):
    """Категории продуктов"""
    name = models.CharField(max_length=64, unique=True, verbose_name='Категория')
    description = models.CharField(max_length=128, blank=True, verbose_name='Описание')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Активна')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Product(models.Model):
    """Продукты"""
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=64, unique=True, verbose_name='Наименование продукта')
    short_desc = models.CharField(max_length=128, blank=True, verbose_name='Краткое описание')
    description = models.TextField('Описание', blank=True)
    price = models.DecimalField('Цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveSmallIntegerField('Количество', default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} ({self.category.name})'


class Images(models.Model):
    """Изображения продуктов"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    upload = models.ImageField(upload_to=product_directory_path)

    class Meta:
        verbose_name = 'Фотография продукта'
        verbose_name_plural = 'Фотографии продуктов'

    def __str__(self):
        return f'Image {self.pk} ({self.product})'


class Contacts(models.Model):
    """Контакты магазинов"""
    city = models.CharField(max_length=128, unique=True, verbose_name='Город')
    address = models.CharField(max_length=256, verbose_name='Адрес')
    phone = models.CharField(max_length=64, verbose_name='Телефон')
    email = models.EmailField()

    def __str__(self):
        return self.city

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
