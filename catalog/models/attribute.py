from django.db import models
from django.utils.text import slugify
from core.models import BaseModel

class ProductAttribute(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product Attribute"
        verbose_name_plural = "Product Attributes"
        db_table = "product_attributes"
    
class ProductAttributeValue(BaseModel):
    attribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE, related_name='values')
    value = models.CharField(max_length=255)

    class Meta:
        unique_together = ('attribute', 'value')
        db_table = "product_attribute_values"
        verbose_name = "Product Attribute Value"
        verbose_name_plural = "Product Attribute Values"

    def __str__(self):
        return f"{self.attribute.name}: {self.value}"


