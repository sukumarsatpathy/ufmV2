from django.contrib import admin
from .models import Product, Style, Variation, ProductGallery


admin.site.register(Product)
admin.site.register(Style)
admin.site.register(Variation)
admin.site.register(ProductGallery)