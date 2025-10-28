from django.db import models
from core.models import BaseModel
from .product import Product

class ProductTag(BaseModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class ProductTagLink(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    tag = models.ForeignKey(ProductTag, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('product', 'tag')

    def __str__(self):
        return f"{self.product.name} → {self.tag.name}"
