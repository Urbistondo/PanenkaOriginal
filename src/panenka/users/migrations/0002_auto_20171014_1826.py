# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='balance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='birth_date',
            field=models.DateTimeField(blank=True, default='1899-01-01 00:00'),
        ),
    ]