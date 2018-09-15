# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-23 14:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0004_auto_20180723_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='userPhonenum',
            field=models.CharField(default=0, max_length=11),
        ),
    ]
    operations = [
        migrations.AddField(
            model_name='comment',
            name='article_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='learn.Article'),
        ),
    ]