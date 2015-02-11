# coding=utf-8
from django.db import models
from tinymce.models import HTMLField
from redactor.fields import RedactorField


# class Category
class Category(models.Model):
    title = models.CharField("Название", max_length=200)
    patent = models.ForeignKey("self", blank=True, default="-1", help_text="Родительская категория", null=True, verbose_name="Родительская категория")
    text = RedactorField(verbose_name="Описание", blank=True)
    description = models.CharField("Description", max_length=200)
    keyword = models.CharField("Ключевые слова", max_length=200)
    url = models.CharField("Url", max_length=200)
    step = models.IntegerField("Вложенность", blank=True, editable=False)
    icon = models.CharField("Иконка", max_length=200, blank=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        unique_together = ("url",)

    def __unicode__(self):
        return self.title

    def get_nameCategory(self):
        return "-" + self.patent.title

    get_nameCategory.admin_order_field = 'product_category'
    get_nameCategory.short_description = 'Категория'

    def get_all_products(self):
        mass_products = []

        def rec_category(obj):
            products = Product.objects.filter(product_category=obj)
            for product in products:
                mass_products.append(product)

            categories = Category.objects.filter(patent=obj)
            for category in categories:
                rec_category(category)

        rec_category(self)
        return mass_products

    def get_all_products_s_year(self, _year):
        mass_products = []

        def rec_category(obj):
            products = Product.objects.filter(product_category=obj, year=_year)
            for product in products:
                mass_products.append(product)

            categories = Category.objects.filter(patent=obj)
            for category in categories:
                rec_category(category)

        rec_category(self)
        return mass_products

    def get_path_categ(self):
        mass_pass = []

        def rec_path(obj):
            if obj is not None:
                mass_pass.append(obj)
                rec_path(obj.patent)

        rec_path(self)
        return mass_pass

    def get_root_categ(self):

        pbeg = self
        while pbeg is not None:
            if pbeg.patent is None:
                return pbeg
            pbeg = pbeg.patent


# class Product
class Product(models.Model):
    title = models.CharField("Название", max_length=200)
    description = RedactorField(verbose_name="Описание")
    keyword = models.CharField("Ключевые слова", max_length=200)
    price = models.CharField("Цена", max_length=200)
    images = models.ImageField("Изображение", upload_to='static/uploadImages/', blank=True)
    product_category = models.ForeignKey(Category, verbose_name="Категория")
    brand = models.CharField("Марка", max_length=200, blank=True)
    year = models.CharField("Год выпуска", max_length=200, blank=True)
    type_body = models.CharField("Тип кузова", max_length=200, blank=True)
    eko_class = models.CharField("Эко/Класс", max_length=200, blank=True)
    transmission = models.CharField("Трансмиссия", max_length=200, blank=True)
    color = models.CharField("Цвет", max_length=200, blank=True)
    power = models.CharField("Мощность (л.с.)", max_length=200, blank=True)
    engine = models.CharField("Объём дв. (см3)", max_length=200, blank=True)
    weight = models.CharField("Тара.Вес (кг)", max_length=200, blank=True)
    suspension = models.CharField("Подвеска", max_length=200, blank=True)
    brake_system = models.CharField("Тормозная система", max_length=200, blank=True)
    public = models.BooleanField("Активен", default=True)
    date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __unicode__(self):
        return self.title

    def get_nameCategory(self):
        return self.product_category.title

    get_nameCategory.short_description = 'Категория'
    get_nameCategory.admin_order_field = 'product_category'

    def get_prew(self):
        return '<img src="/' + str(self.images) + '" style="height:40px"/>'

    get_prew.allow_tags = True
    get_prew.short_description = 'Изображение'


class Image(models.Model):
    product = models.ForeignKey(Product)
    image = models.FileField("Изображение", upload_to='static/uploadImages/', blank=True)
