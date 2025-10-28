from django.shortcuts import render
from catalog.models import Product, Category

def home_view(request):
    """Home page view"""
    try:
        featured_products = Product.objects.all()[:6]  # Get first 6 products
        categories = Category.objects.filter(status=True)[:5]  # Get first 5 active categories
    except:
        # Fallback if tables don't exist yet
        featured_products = []
        categories = []
    
    return render(request, 'home.html', {
        'featured_products': featured_products,
        'categories': categories,
        'page_title': 'Welcome to Alpha Jewelry'
    })
