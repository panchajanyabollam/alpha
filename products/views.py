from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product, ProductCategory

def product_list(request):
    """Display all products"""
    products = Product.objects.all()
    return render(request, 'products/list.html', {
        'products': products,
        'page_title': 'All Products'
    })

def product_detail(request, product_id):
    """Display single product detail"""
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/detail.html', {
        'product': product,
        'page_title': product.title
    })

def products_by_category(request, category_id):
    """Display products filtered by category"""
    category = get_object_or_404(ProductCategory, id=category_id)
    products = Product.objects.filter(category=category)
    return render(request, 'products/list.html', {
        'products': products,
        'category': category,
        'page_title': f'Products in {category.name}'
    })

def home_view(request):
    """Home page view"""
    featured_products = Product.objects.all()[:6]  # Get first 6 products
    categories = ProductCategory.objects.filter(is_active=True)[:5]
    return render(request, 'home.html', {
        'featured_products': featured_products,
        'categories': categories,
        'page_title': 'Welcome to Alpha Jewelry'
    })

def launch(request):
    """Launch page view"""
    return render(request, 'launch.html', {
        'page_title': 'Website Launch'
    })
