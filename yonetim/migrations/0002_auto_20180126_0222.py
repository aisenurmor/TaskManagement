# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-25 23:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yonetim', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Görevler', 'verbose_name_plural': 'Görevler'},
        ),
    ]