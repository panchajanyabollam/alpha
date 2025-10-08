from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    """
    Product categories like Rings, Chains, Pendants, etc.
    """
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'
        ordering = ['name']
    
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.TextField()
    description = models.TextField()
    price = models.FloatField()
    summary = models.TextField(default="This is a great product.")
    image_url = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="URL of the product image"
    )
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        related_name='products',
        null=True,
        blank=True,
        help_text="Product category (Rings, Chains, etc.)"
    )
    
    def __str__(self):
        return self.title