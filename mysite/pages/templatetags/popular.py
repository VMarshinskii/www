from django import template
from catalog.models import Product

register = template.Library()

@register.inclusion_tag('popular.html')
def popular():
    objects = Product.objects.order_by('?').all()[: 6]
    return {'objects': objects}