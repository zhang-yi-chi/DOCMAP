# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0006_auto_20160424_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='priority',
            field=models.IntegerField(default=3),
        ),
    ]
