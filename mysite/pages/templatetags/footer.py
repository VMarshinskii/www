from django import template
from settings.models import Settings

register = template.Library()

@register.inclusion_tag('footer.html')
def footer():
    model = Settings.objects.get(id=1)
    return {'settings': model}