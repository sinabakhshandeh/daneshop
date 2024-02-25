from django.contrib import admin

from shop.models import Media, Product, ProductCategory, ProductPrice

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductPrice)
admin.site.register(Media)
