# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-08 20:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_merge_20170807_1431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end_date_and_time',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date_and_time',
            field=models.CharField(max_length=20),
        ),
    ]
