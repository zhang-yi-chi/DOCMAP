# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 04:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0004_auto_20160424_0358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='descrpition',
            new_name='descrption',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='descrpition',
            new_name='descrption',
        ),
    ]
