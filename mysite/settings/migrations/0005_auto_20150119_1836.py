# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0004_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='map',
            field=models.TextField(verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xb4 \xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd1\x8b', blank=True),
            preserve_default=True,
        ),
    ]
