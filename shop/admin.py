from django.contrib import admin

from shop.models import Product, ProductCategory, ProductMedia, ProductPrice

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductPrice)
admin.site.register(ProductMedia)
