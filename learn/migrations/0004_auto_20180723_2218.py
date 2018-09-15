# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-23 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0003_auto_20180721_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userPhonenum',
            field=models.CharField(default='', max_length=11),
        ),
        migrations.AlterField(
            model_name='user',
            name='userEmail',
            field=models.EmailField(max_length=30),
        ),
    ]