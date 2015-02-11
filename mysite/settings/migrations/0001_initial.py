# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x81\xd0\xb0\xd0\xb9\xd1\x82\xd0\xb0')),
                ('description', models.TextField(max_length=200, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x81\xd0\xb0\xd0\xb9\xd1\x82\xd0\xb0')),
                ('phone_home', models.CharField(max_length=200, verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xbb. \xd0\xb2 \xd1\x88\xd0\xb0\xd0\xbf\xd0\xba\xd0\xb5')),
                ('email', models.TextField(max_length=200, verbose_name=b'E-mail')),
                ('contacts', models.TextField(max_length=200, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbd\xd1\x82\xd0\xb0\xd0\xba\xd1\x82\xd1\x8b')),
                ('odnoklassniki', models.TextField(max_length=200, verbose_name=b'\xd0\x9e\xd0\xb4\xd0\xbd\xd0\xbe\xd0\xba\xd0\xbb\xd0\xb0\xd1\x81\xd1\x81\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb8')),
                ('twitter', models.TextField(max_length=200, verbose_name=b'Twitter')),
                ('facebook', models.TextField(max_length=200, verbose_name=b'Facebook')),
                ('vk', models.TextField(max_length=200, verbose_name=b'\xd0\x92\xd0\xba\xd0\xbe\xd0\xbd\xd1\x82\xd0\xb0\xd0\xba\xd1\x82\xd0\xb5')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
