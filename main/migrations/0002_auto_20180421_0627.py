# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-21 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='is_acitve',
            field=models.BooleanField(default=True),
        ),
    ]
