# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minerals', '0003_auto_20170215_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='mineral',
            name='group',
            field=models.CharField(default='', max_length=255),
        ),
    ]
