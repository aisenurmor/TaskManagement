# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-25 23:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('resolved_date', models.DateTimeField()),
                ('assignee', models.TextField()),
                ('status', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=200)),
            ],
        ),
    ]