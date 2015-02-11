from django import template
from clients.models import Client

register = template.Library()

@register.inclusion_tag('clients_left.html')
def clients_left():
    objects = Client.objects.order_by('?').all()
    return {'objects': objects}