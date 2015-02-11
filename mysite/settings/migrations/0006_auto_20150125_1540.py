# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_auto_20150119_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='footer',
            field=models.TextField(default=b'qwe', verbose_name=b'\xd0\xa2\xd0\xb5\xd0\xba\xd1\x81\xd1\x82 \xd0\xb2 \xd1\x84\xd1\x83\xd1\x82\xd0\xb5\xd1\x80\xd0\xb5', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='settings',
            name='footer_link',
            field=models.TextField(default=12, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xb4 \xd1\x81\xd1\x87\xd1\x91\xd1\x82\xd1\x87\xd0\xb8\xd0\xba\xd0\xbe\xd0\xb2 \xd0\xb2 \xd1\x84\xd1\x83\xd1\x82\xd0\xb5\xd1\x80\xd0\xb5', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='settings',
            name='contacts',
            field=models.TextField(verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xbd\xd1\x82\xd0\xb0\xd0\xba\xd1\x82\xd1\x8b', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='facebook',
            field=models.CharField(max_length=200, verbose_name=b'Facebook', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='odnoklassniki',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x9e\xd0\xb4\xd0\xbd\xd0\xbe\xd0\xba\xd0\xbb\xd0\xb0\xd1\x81\xd1\x81\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb8', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='twitter',
            field=models.CharField(max_length=200, verbose_name=b'Twitter', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='settings',
            name='vk',
            field=models.CharField(max_length=200, verbose_name=b'\xd0\x92\xd0\xba\xd0\xbe\xd0\xbd\xd1\x82\xd0\xb0\xd0\xba\xd1\x82\xd0\xb5', blank=True),
            preserve_default=True,
        ),
    ]
