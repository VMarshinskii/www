# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'\xd0\x98\xd0\xbc\xd1\x8f \xd0\xba\xd0\xbb\xd0\xb8\xd0\xb5\xd0\xbd\xd1\x82\xd0\xb0')),
                ('image', models.ImageField(upload_to=b'static/uploadImages/', verbose_name=b'\xd0\x98\xd0\xb7\xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb6\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
            ],
            options={
                'verbose_name': '\u041a\u043b\u0438\u0435\u043d\u0442',
                'verbose_name_plural': '\u041a\u043b\u0438\u0435\u043d\u0442\u044b',
            },
            bases=(models.Model,),
        ),
    ]
