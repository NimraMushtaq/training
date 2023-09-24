from django.shortcuts import get_object_or_404
from products.models import Product, WishlistItem
from products.serializers import ProductSerializer, WishlistSerializer
from rest_framework import generics, status, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class IsOwnerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    lookup_url_kwarg = 'product_id'
    queryset = Product.objects.all()

    def get_queryset(self):
        queryset = Product.objects.all()

        color = self.request.query_params.get('color', None)
        brand = self.request.query_params.get('brand', None)

        if color:
            queryset = queryset.filter(color__iexact=color)
        if brand:
            queryset = queryset.filter(brand__iexact=brand)

        return queryset

    def get(self, request, *args, **kwargs):
        product_id = kwargs.get(self.lookup_url_kwarg)
        if product_id:
            product = generics.get_object_or_404(self.queryset, id=product_id)
            serializer = self.get_serializer(product)
            return Response(serializer.data)
        return super().list(request, *args, **kwargs)


class WishlistAPIView(generics.ListCreateAPIView, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsOwnerPermission]
    serializer_class = WishlistSerializer
    queryset = WishlistItem.objects.all()

    def get_queryset(self):
        user = self.request.user
        return WishlistItem.objects.filter(user=user)

    def list(self, request, *args, **kwargs):
        wishlist_item_id = kwargs.get('wishlist_item_id')

        if wishlist_item_id is not None:
            return self.destroy(request, *args, **kwargs)
        else:
            return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        user = request.user
        product = get_object_or_404(Product, pk=product_id)
        wishlist_item, created = WishlistItem.objects.get_or_create(user=user, product=product)

        if not created:
            return Response(
                {'message': 'Product already in wishlist.'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {'message': 'Product added to wishlist.'},
                status=status.HTTP_201_CREATED
            )

    def destroy(self, request, *args, **kwargs):
        wishlist_item = get_object_or_404(WishlistItem, pk=kwargs['wishlist_item_id'])
        wishlist_item.delete()

        return Response(
            {'message': 'Wishlist item removed successfully.'},
            status=status.HTTP_204_NO_CONTENT
        )
