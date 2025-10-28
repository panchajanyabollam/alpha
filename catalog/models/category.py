from django.db import models
from django.utils.text import slugify
from core.models import BaseModel

class Category(BaseModel):

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    parent = models.ForeignKey('self', null = True, blank = True, on_delete=models.SET_NULL, related_name='subcategories')
    description = models.TextField(blank=True, null=True)
    image_url  = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        help_text="URL of the category image"
    )
    status = models.BooleanField(default=True, help_text="Designates whether this category is active")

    class Meta:
        verbose_name_plural = "Product Categories"
        db_table = "product_categories"
        unique_together = ('parent', 'slug')


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        if self.parent:
            return f"{self.parent.name} -> {self.name}"
        return self.name