from django.contrib import admin
from .models import Product, ProductCategory

# Register ProductCategory admin
@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('is_active', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
    prepopulated_fields = {'name': ('name',)}

# Register Product admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'image_url')
    search_fields = ('title', 'description')
    list_filter = ('category', 'price')
    readonly_fields = ('id',)
    autocomplete_fields = ['category']
