from django.shortcuts import render_to_response
from orders.models import Order
from django.http import Http404, HttpResponse
from catalog.models import Product


# Create your views here.
def place(request):
    name = request.GET.get('name')
    phone = request.GET.get('phone')
    email = request.GET.get('email')
    id = request.GET.get('id')

    order = Order()
    order.name = name
    order.phone = phone
    order.email = email
    order.product_id = Product.objects.get(id=id)

    order.save()

    return render_to_response('place_order.html')