from django.db import models
from core.models import BaseModel
from .category import Category
from django.utils.text import slugify

class Product(BaseModel):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    # Stock Keeping Unit
    sku = models.CharField(max_length=100, unique=True)
    status = models.BooleanField(default=True, help_text="Designates whether this product is active")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        db_table = "products"
        ordering = ['name']
        

