# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f', max_length=200, editable=False)),
                ('phone', models.CharField(verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd', max_length=200, editable=False)),
                ('email', models.CharField(verbose_name=b'E-mail', max_length=200, editable=False, blank=True)),
                ('product_id', models.IntegerField(verbose_name=b'\xd0\x97\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0\xd0\xbd', editable=False, blank=True)),
                ('date', models.DateField(auto_now=True, verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
