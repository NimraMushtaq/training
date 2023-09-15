import json
import os
from products.models import Product, LaptopSpecs, AirpodSpecs

def load_airpods_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(script_dir, 'json_files/airpods.json')

    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    for product_data in data:
        # Create a Product instance
        product = Product(
            name=product_data['name'],
            brand=product_data['brand'],
            color=product_data['color'],
            price=product_data['price'],
            product_type=1  # Assuming Airpods have a product_type of 1
        )
        product.save()
        airpod = AirpodSpecs(
            product=product
        )
        airpod.save()

def load_laptops_data():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(script_dir, 'json_files/laptops.json')

    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    for product_data in data:
        # Create a Product instance
        product = Product(
            name=product_data['name'],
            brand=product_data['brand'],
            color=product_data['color'],
            price=product_data['price'],
            product_type=2
        )
        product.save()

        laptop = LaptopSpecs(
            product=product,
            screen_resolution=product_data['screen_resolution'],
            screen_size=product_data['screen_size'],
            ssd=product_data['ssd'],
            installed_ram=product_data['installed_ram'],
            generation=product_data['generation'],
            weight=product_data['weight'],
        )
        laptop.save()
