# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-09-14 12:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0009_auto_20180914_2050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article',
            new_name='article_id',
        ),
    ]
