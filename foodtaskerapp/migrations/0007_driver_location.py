# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-22 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtaskerapp', '0006_auto_20171210_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='location',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
