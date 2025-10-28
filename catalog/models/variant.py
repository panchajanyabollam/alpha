from django.db import models
from core.models import BaseModel
from .product import Product
from .attribute import ProductAttributeValue

class ProductVariant(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variants')
    sku = models.CharField(max_length=100, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="URL of the variant image"
    )
    status = models.BooleanField(default=True, help_text="Designates whether this variant is active")

    def __str__(self):
        return f"{self.product.name} - {self.sku}"

    class Meta:
        verbose_name = "Product Variant"
        verbose_name_plural = "Product Variants"
        db_table = "product_variants"
        ordering = ['product__name', 'sku']

class ProductVariantAttributeValue(BaseModel):
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name='attribute_values')
    attribute_value = models.ForeignKey(ProductAttributeValue, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('variant', 'attribute_value')
        db_table = "product_variant_attribute_values"
        verbose_name = "Product Variant Attribute Value"
        verbose_name_plural = "Product Variant Attribute Values"

    def __str__(self):
        return f"{self.variant.sku} - {self.attribute_value}"