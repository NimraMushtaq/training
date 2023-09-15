from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    PRODUCT_TYPES = [
        (1, 'Airpods'),
        (2, 'Laptop'),
    ]
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    product_type = models.PositiveSmallIntegerField(choices=PRODUCT_TYPES)
    price = models.FloatField()

    def __str__(self):
        return self.name


class AirpodSpecs(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class LaptopSpecs(models.Model):
    screen_resolution = models.CharField(max_length=255)
    screen_size = models.CharField(max_length=255)
    ssd = models.CharField(max_length=255)
    installed_ram = models.CharField(max_length=255)
    generation = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class WishlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s wishlist: {self.product.name} "
