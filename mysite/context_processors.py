from products.models import ProductCategory

def header_context(request):
    """
    Context processor to provide common header data to all templates
    """
    return {
        'header_categories': ProductCategory.objects.filter(is_active=True).order_by('name')[:10],
    }