from django import template
from pages.models import Page, Section

register = template.Library()

@register.inclusion_tag('admin_menu.html')
def admin_menu():
    message = "Hello"

    return {'oll_pages': message}