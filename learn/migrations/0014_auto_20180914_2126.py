# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-09-14 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0013_auto_20180914_2106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article',
            new_name='article_id',
        ),
        migrations.AlterField(
            model_name='user',
            name='userPhonenum',
            field=models.CharField(default=0, max_length=11),
        ),
    ]