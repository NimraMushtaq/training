from django.urls import path
from products.views import ProductListView, WishlistAPIView

urlpatterns = [

    path('api/products/', ProductListView.as_view(), name='product-search'),
    path('api/products/<int:product_id>/', ProductListView.as_view(), name='product-detail'),
    path('api/wishlistItem/', WishlistAPIView.as_view(), name='wishlist-api'),
    path('api/wishlistItem/<int:wishlist_item_id>/', WishlistAPIView.as_view(), name='wishlist-item-delete'),

]
