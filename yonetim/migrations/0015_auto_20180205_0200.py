# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-04 23:00
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yonetim', '0014_auto_20180205_0024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='İçerik'),
        ),
    ]
