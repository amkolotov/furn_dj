import json
import os

from django.core.management import BaseCommand

from main_app.models import ProductCategory, Product, Images, Contacts

JSON_PATH = 'main_app/db_json'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name)) as file:
        return json.load(file)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        categories = load_from_json('categories.json')
        ProductCategory.objects.all().delete()

        for category in categories:
            ProductCategory.objects.create(**category)

        products = load_from_json('products.json')
        Product.objects.all().delete()

        for product in products:
            category_name = product['category']
            _category = ProductCategory.objects.get(name=category_name)
            product['category'] = _category
            Product.objects.create(**product)

        images = load_from_json('images.json')
        Images.objects.all().delete()

        for image in images:
            product_name = image['product']
            _product = Product.objects.get(name=product_name)
            image['product'] = _product
            Images.objects.create(**image)

        contacts = load_from_json('contacts.json')
        Contacts.objects.all().delete()

        for contanct in contacts:
            Contacts.objects.create(**contanct)




