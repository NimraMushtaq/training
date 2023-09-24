import json
import os
from products.models import Product, LaptopSpecs, AirpodSpecs


def load_airpods_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(script_dir, 'json_files/airpods.json')

    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    product_list = []
    airpod_list = []

    for product_data in data:
        product = Product(
            name=product_data['name'],
            brand=product_data['brand'],
            color=product_data['color'],
            price=product_data['price'],
            product_type=Product.AIRPOD
        )
        product_list.append(product)

    Product.objects.bulk_create(product_list)

    saved_products = Product.objects.filter(name__in=[product.name for product in product_list])

    for product_data, saved_product in zip(data, saved_products):
        airpod = AirpodSpecs(
            product=saved_product
        )
        airpod_list.append(airpod)

    AirpodSpecs.objects.bulk_create(airpod_list)


def load_laptops_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(script_dir, 'json_files/laptops.json')

    with open(json_file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    product_list = []
    laptop_list = []

    for product_data in data:
        product = Product(
            name=product_data['name'],
            brand=product_data['brand'],
            color=product_data['color'],
            price=product_data['price'],
            product_type=Product.LAPTOP
        )
        product_list.append(product)

    Product.objects.bulk_create(product_list)

    saved_products = Product.objects.filter(name__in=[product.name for product in product_list])

    for product_data, saved_product in zip(data, saved_products):
        laptop = LaptopSpecs(
            product=saved_product,
            screen_resolution=product_data['screen_resolution'],
            screen_size=product_data['screen_size'],
            ssd=product_data['ssd'],
            installed_ram=product_data['installed_ram'],
            generation=product_data['generation'],
            weight=product_data['weight'],
        )
        laptop_list.append(laptop)

    LaptopSpecs.objects.bulk_create(laptop_list)
