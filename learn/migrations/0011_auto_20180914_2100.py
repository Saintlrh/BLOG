# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-09-14 13:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0010_auto_20180914_2051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article_id',
            new_name='article_from',
        ),
    ]
