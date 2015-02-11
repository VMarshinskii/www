# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.CharField(max_length=200, verbose_name=b'E-mail', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='product_id',
            field=models.IntegerField(verbose_name=b'\xd0\x97\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0\xd0\xbd', blank=True),
            preserve_default=True,
        ),
    ]
