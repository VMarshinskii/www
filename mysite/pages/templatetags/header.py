from django import template
from settings.models import Settings

register = template.Library()

@register.inclusion_tag('header.html')
def header():
    model = Settings.objects.get(id=1)
    return {'meta_model': model}