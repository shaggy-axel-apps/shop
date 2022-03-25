from django.db import models


class ProductCategory(models.Model):
    title = models.CharField(max_length=32)
    description = models.TextField(default='')

    class Meta:
        db_table = 'product-categories'

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default='')
    category = models.ForeignKey(
        ProductCategory, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    quantity = models.IntegerField(default=0)
    photo = models.ImageField(upload_to="products", blank=True, null=True)

    class Meta:
        db_table = 'products'

    def __str__(self) -> str:
        return self.title
