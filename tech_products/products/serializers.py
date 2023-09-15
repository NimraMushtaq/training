from products.models import Product, WishlistItem
from users.serializers import UserSerializer
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class WishlistSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    product = ProductSerializer()

    class Meta:
        model = WishlistItem
        fields = ['id', 'user', 'product']
