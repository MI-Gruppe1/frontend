# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-12-05 17:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20161010_1729'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherStation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wid', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('location_lat', models.FloatField(default=0)),
                ('location_lon', models.FloatField(default=0)),
            ],
        ),
    ]