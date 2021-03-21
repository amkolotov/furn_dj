from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField


class ShopUser(AbstractUser):
    """Модель пользователя"""
    pass


class ShopUserProfile(models.Model):
    """Профиль пользователя"""
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = ((MALE, 'М'), (FEMALE, 'Ж'))

    user = models.OneToOneField(ShopUser, unique=True, null=False, db_index=True, on_delete=models.CASCADE)
    phone = PhoneNumberField('Номер телефона', blank=True,
                             error_messages={'invalid': 'Введите номер по образцу: +79120000000'})
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, verbose_name='Пол')
    about_me = models.TextField('О себе', blank=True)
    date_of_birth = models.DateField('Дата рождения', blank=True, null=True)
    avatar = models.ImageField('Аватар', upload_to='users_avatar', default='users_avatar/default_avatar.jpg')

    @receiver(post_save, sender=ShopUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            ShopUserProfile.objects.create(user=instance)

    @receiver(post_save, sender=ShopUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.shopuserprofile.save()

    class Meta:
        verbose_name = 'Профайл'
        verbose_name_plural = 'Профайлы'

    def __str__(self):
        return f'Profile - {self.user}'
