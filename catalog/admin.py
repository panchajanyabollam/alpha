from django.contrib import admin

from .models import (ProductAttribute,
 ProductAttributeValue,
Category,
ProductImage,
Product,
ProductTag,
ProductTagLink,
ProductVariant,
ProductVariantAttributeValue)

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductVariant)
admin.site.register(ProductVariantAttributeValue)
admin.site.register(ProductAttribute)
admin.site.register(ProductAttributeValue)
admin.site.register(ProductTag)
admin.site.register(ProductTagLink)

