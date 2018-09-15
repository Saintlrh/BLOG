# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-09-14 11:34
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0007_auto_20180812_2113'),
    ]

    operations = [
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateTimeField()),
                ('content', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='内容')),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
    ]
