import random

from django.core.management import BaseCommand

from auth_app.models import ShopUser, ShopUserProfile
from main_app.models import Product, Reviews


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users = (
            {'username': 'Alex', 'avatar': 'alex_ava.jpg'},
            {'username': 'John', 'avatar': 'john_ava.jpg'},
            {'username': 'Kate', 'avatar': 'kate_ava.jpg'},
        )
        reviews = (
            'Хороший товар',
            'Соответствует описанию',
            'На троечку',
            'Полностью оправдал ожидания',
            'Цена немного завышена',
            'Качественный товар',
            'Цена соответствует качеству',
            'Некачественный товар',
        )

        new_users = []
        for user in users:
            old_user = ShopUser.objects.filter(username=user['username'])
            if old_user:
                old_user.delete()
            new_user = ShopUser.objects.create(username=user['username'], password=f'django{user["username"]}')
            profile = ShopUserProfile.objects.get(user=new_user)
            profile.avatar = f'users_avatar/{user["avatar"]}'
            profile.save()
            new_users.append(new_user)

        products = Product.objects.all()

        Reviews.objects.all().delete()

        for product in products:
            random.shuffle(new_users)
            review_id = None
            for i in range(len(new_users)):
                if i % 2 == 0:
                    review = Reviews.objects.create(
                        product=product,
                        user=new_users[i],
                        text=random.choice(reviews)
                    )
                    review_id = review.id
                else:
                    Reviews.objects.create(
                        product=product,
                        user=new_users[i],
                        parent_id=review_id,
                        text=random.choice(reviews)
                    )




