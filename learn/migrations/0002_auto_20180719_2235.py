# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-19 14:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userPassword',
            field=models.CharField(max_length=100),
        ),
    ]
