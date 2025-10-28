from catalog.models import Category, Product
from django.db.models import Count

def header_context(request):
    """
    Context processor to provide common header data to all templates
    """
    try:
        return {
            # Categories for navigation dropdown
            'header_categories': Category.objects.filter(status=True).order_by('name')[:10],
            
            # Site-wide statistics
            'site_stats': {
                'total_products': Product.objects.count(),
                'total_categories': Category.objects.filter(status=True).count(),
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
    except:
        # Fallback if catalog models don't exist yet
        return {
            'header_categories': [],
            'site_stats': {
                'total_products': 0,
                'total_categories': 0,
            },
            'is_admin_user': request.user.is_staff if request.user.is_authenticated else False,
            'site_config': {
                'site_name': 'Alpha Jewelry',
                'company_phone': '+1-234-567-8900',
                'company_email': 'info@alphajewelry.com',
            }
        }