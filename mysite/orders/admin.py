from django.contrib import admin
from orders.models import Order


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'get_product', 'date')
    list_filter = ('date',)
    search_fields = ['title']
    date_hierarchy = 'date'


admin.site.register(Order, OrderAdmin)