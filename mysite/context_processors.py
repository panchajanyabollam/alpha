from products.models import ProductCategory, Product
from django.db.models import Count

def header_context(request):
    """
    Context processor to provide common header data to all templates
    """
    return {
        # Categories for navigation dropdown
        'header_categories': ProductCategory.objects.filter(is_active=True).order_by('name')[:10],
        
        # Site-wide statistics
        'site_stats': {
            'total_products': Product.objects.count(),
            'total_categories': ProductCategory.objects.filter(is_active=True).count(),
        },
        
        # Current user context (additional to built-in auth)
        'is_admin_user': request.user.is_staff if request.user.is_authenticated else False,
        
        # Site configuration
        'site_config': {
            'site_name': 'Alpha Jewelry',
            'company_phone': '+1-234-567-8900',
            'company_email': 'info@alphajewelry.com',
        }
    }