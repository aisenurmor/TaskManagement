# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-13 12:32
from __future__ import unicode_literals

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180213_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profil_photo',
            field=models.ImageField(blank=True, default='static/img/default.png', upload_to=users.models.upload_to, verbose_name='Profil Fotoğrafı'),
        ),
    ]
