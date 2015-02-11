from django.shortcuts import render_to_response
from catalog.models import Product, Category, Image
from settings.models import Settings
from catalog.admin import sort_list
from django.http import Http404, HttpResponse
import json as simplejson


# Create your views here.
def home(request):
    categories = Category.objects.order_by('id').filter(patent=None)
    res_mass = {}
    for categ in categories:
        res_mass[categ] = categ.get_all_products()[:3]

    return render_to_response("index.html", {'products': res_mass, 'meta_model': Settings.objects.get(id=1)})


def category(request, categ_name=1):
    try:
        categ = Category.objects.get(url=categ_name)
        products = categ.get_all_products()
        path_categ = categ.get_path_categ()
        root_categ = categ.get_root_categ()

    except Category.DoesNotExist:
        raise Http404
    return render_to_response("category.html", {
        'products': products,
        'path_categ': path_categ,
        'categ': categ,
        'root_categ': root_categ,
        'left_categories': Category.objects.filter(patent=root_categ)
    })


def catalog(request):
    categories = Category.objects.order_by('id').filter(patent=None)
    res_mass = {}
    for categ in categories:
        res_mass[categ] = categ.get_all_products()[:3]

    return render_to_response("index.html", {'products': res_mass})


def product(request, categ_name=1, product_id=1):
    try:
        product_current = Product.objects.get(id=product_id)
        root_categ = product_current.product_category.get_root_categ()
        images = Image.objects.filter(product=product_current)
    except Product.DoesNotExist:
        raise Http404
    return render_to_response("product.html", {
        'product': product_current,
        'root_categ': root_categ,
        'images': images
    })


def ajax_filter(request):
    type = request.GET.get('type')
    year = request.GET.get('year')
    model = request.GET.get('model')
    products = Product.objects.all()

    if type != "-1":
        categ = Category.objects.get(id=type)
        products = categ.get_all_products()

    if year != "-1":
        products_new = []
        for pr in products:
            if pr.year == year:
                products_new.append(pr)
        products = products_new

    if model != "-1":
        products_new = []
        for pr in products:
            if pr.brand == model:
                products_new.append(pr)
        products = products_new


    return render_to_response("ajax_filter.html", {
        'products': products,
        'type': type,
        'year': year,
        'model': model
    })


def ajax_all_categories(request):
    try:
        categories = sort_list()
        model = Product.objects.get(request.GET.get('id'))
    except Product.DoesNotExist:
        raise Http404
    return render_to_response("admin/ajax_all_categories.html", {'categories': categories, 'model': model})