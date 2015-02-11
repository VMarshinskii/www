from django import template
from catalog.models import Category, Product

register = template.Library()

@register.inclusion_tag('search_form.html')
def search_form():
    types = Category.objects.order_by('id').filter(patent=None)
    objects = Product.objects.order_by('year').all()

    mass_year = []
    mass_model = []
    for obj in objects:
        mass_year.append(obj.year)
        mass_model.append(obj.brand)

    mass_year = list(set(mass_year))
    mass_model = list(set(mass_model))


    return {'types': types, 'years': mass_year, 'models': mass_model}