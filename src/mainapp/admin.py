from django.contrib import admin

from mainapp.models import Product


@admin.register(Product)
class Product(admin.ModelAdmin):
    pass
