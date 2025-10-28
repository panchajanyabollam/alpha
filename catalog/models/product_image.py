from django.db import models
from core.models import BaseModel
from .product import Product
from .variant import ProductVariant

class ProductImage(BaseModel):

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images'
    )

    variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE,
        related_name='variant_images',
        null=True,
        blank=True,
        help_text="Optional. Attach to a specific variant."
    )

    image_url = models.URLField(
        help_text="Absolute or relative URL of the image file."
    )

    alt_text = models.CharField(
        max_length=255,
        blank=True,
        help_text="Alternative text for SEO and accessibility."
    )

    is_primary = models.BooleanField(
        default=False,
        help_text="Marks the main display image."
    )

    sort_order = models.PositiveIntegerField(
        default=0,
        help_text="Used to order images in the gallery."
    )

    class Meta:
        db_table = 'product_images'
        ordering = ['sort_order']
        verbose_name = 'Product Image'
        verbose_name_plural = 'Product Images'

    def __str__(self):
        return f"Image for {self.product.name}" + (f" ({self.variant.sku})" if self.variant else "")
