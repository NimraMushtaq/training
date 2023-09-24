from django.contrib import admin
from products.models import Product, LaptopSpecs, AirpodSpecs, WishlistItem


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'color', 'product_type', 'price')
    list_filter = ('brand', 'product_type')
    search_fields = ('name', 'brand', 'color')


class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product',)


class LaptopSpecsAdmin(admin.ModelAdmin):
    list_display = (
        'screen_resolution', 'screen_size', 'ssd', 'installed_ram', 'generation',
        'weight',
    )
    list_filter = ('product__brand',)
    search_fields = (
        'screen_resolution', 'screen_size', 'ssd', 'installed_ram', 'generation', 'weight'
    )


admin.site.register(WishlistItem, WishlistItemAdmin)
admin.site.register(LaptopSpecs, LaptopSpecsAdmin)
admin.site.register(Product, ProductAdmin)

# Configure Admin Titles
admin.site.site_header = 'Ecommerce Administration'
admin.site.site_title = 'Ecommerce'
admin.site.index_title = 'Admin Area'
