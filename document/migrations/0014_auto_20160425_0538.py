# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-25 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0013_auto_20160425_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='dir',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='link',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='document',
            name='publish_time',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]