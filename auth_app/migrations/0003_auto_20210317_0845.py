# Generated by Django 3.1.7 on 2021-03-17 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_shopuserprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuserprofile',
            name='avatar',
            field=models.ImageField(default='users_avatar/default_avatar.jpg', upload_to='users_avatar', verbose_name='Аватар'),
        ),
    ]
