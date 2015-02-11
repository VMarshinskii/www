# coding=utf-8
from django.db import models


# Create your models here.
class Client(models.Model):
    title = models.CharField("Имя клиента", max_length=200)
    image = models.ImageField("Изображение", upload_to='static/uploadImages/', blank=True)

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __unicode__(self):
        return self.title

class Company(models.Model):
    title = models.CharField("Название компании", max_length=200)
    image = models.ImageField("Изображение", upload_to='static/uploadImages/', blank=True)

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __unicode__(self):
        return self.title