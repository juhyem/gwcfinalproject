# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-07 20:06
from __future__ import unicode_literals

from django.db import migrations, models
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_auto_20170807_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.FileField(blank=True, default='http://i.imgur.com/l8dsevv.png', null=True, upload_to=events.models.upload_location),
        ),
    ]
