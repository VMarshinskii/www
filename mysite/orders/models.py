# coding=utf-8
from django.db import models
from catalog.models import Product


# Create your models here.
class Order(models.Model):
    name = models.CharField("Имя", max_length=200)
    phone = models.CharField("Телефон", max_length=200)
    email = models.CharField("E-mail", max_length=200, blank=True)
    product_id = models.ForeignKey(Product, verbose_name="Заказан")
    date = models.DateField("Дата заказа", auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __unicode__(self):
        return self.name

    def get_product(self):
        return '<a target=_blank href="/catalog/' + str(self.product_id.product_category.url) + '/' + str(self.product_id.id) + '/">' + str(self.product_id.title) + '</a>'

    get_product.allow_tags = True
    get_product.short_description = 'Заказ'