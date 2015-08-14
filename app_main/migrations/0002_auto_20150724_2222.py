# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fio',
            name='age',
            field=models.IntegerField(verbose_name='Вoзраст'),
        ),
        migrations.AlterField(
            model_name='fio',
            name='desc',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='fio',
            name='mail',
            field=models.EmailField(max_length=40, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='fio',
            name='per1',
            field=models.FloatField(verbose_name='Процент'),
        ),
        migrations.AlterField(
            model_name='fio',
            name='phone',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Телефон'),
        ),
    ]
