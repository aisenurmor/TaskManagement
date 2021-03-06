# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-28 10:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yonetim', '0007_auto_20180126_0305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='resolved_date',
        ),
        migrations.AddField(
            model_name='task',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='Taslak Oluştursun mu?'),
        ),
        migrations.AddField(
            model_name='task',
            name='update_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Güncelleme Tarihi'),
        ),
        migrations.AlterField(
            model_name='task',
            name='assignee',
            field=models.ManyToManyField(to='yonetim.Assignee', verbose_name='Görevli'),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ManyToManyField(related_name='task', to='yonetim.Category', verbose_name='Kategori'),
        ),
        migrations.AlterField(
            model_name='task',
            name='content',
            field=models.TextField(verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='task',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Oluşturma Tarihi'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ManyToManyField(to='yonetim.Status', verbose_name='Durum'),
        ),
        migrations.AlterField(
            model_name='task',
            name='summary',
            field=models.CharField(max_length=200, verbose_name='Başlık'),
        ),
    ]
