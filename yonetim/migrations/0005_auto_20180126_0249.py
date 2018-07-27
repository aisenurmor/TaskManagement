# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-25 23:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yonetim', '0004_auto_20180126_0242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignee_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Görevli',
                'verbose_name_plural': 'Görevli',
            },
        ),
        migrations.RemoveField(
            model_name='task',
            name='assignee',
        ),
        migrations.AddField(
            model_name='task',
            name='assignee',
            field=models.ManyToManyField(to='yonetim.Assignee'),
        ),
    ]
