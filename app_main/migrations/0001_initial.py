# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import app_main.models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FIO',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя')),
                ('age', models.IntegerField(verbose_name='Вщзраст')),
                ('date_brd', models.DateTimeField(verbose_name='Дата рождения')),
                ('phone', models.CharField(max_length=30, blank=True, null=True)),
                ('mail', models.EmailField(max_length=40)),
                ('desc', models.TextField()),
                ('per1', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('file', sorl.thumbnail.fields.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', app_main.models.CurrencyField(decimal_places=2, max_digits=10)),
                ('receive_news', models.BooleanField(default=True, db_index=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, db_index=True)),
                ('votes', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='image',
            name='item',
            field=models.ForeignKey(to='app_main.Item'),
        ),
    ]
