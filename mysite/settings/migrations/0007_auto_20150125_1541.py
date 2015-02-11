# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0006_auto_20150125_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='settings',
            name='footer',
        ),
        migrations.RemoveField(
            model_name='settings',
            name='footer_link',
        ),
    ]
