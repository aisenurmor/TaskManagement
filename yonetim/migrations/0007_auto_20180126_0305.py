# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-26 00:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yonetim', '0006_auto_20180126_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ManyToManyField(related_name='task', to='yonetim.Category'),
        ),
    ]
