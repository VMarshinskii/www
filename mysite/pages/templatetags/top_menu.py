from django import template
from pages.models import Page, Section

register = template.Library()

@register.inclusion_tag('top_menu.html')
def show_prod():
    mass_res = {}
    sectoins = Section.objects.all()

    for sec in sectoins:
        mass_res[sec] = Page.objects.filter(section=sec)

    return {'oll_pages': mass_res}