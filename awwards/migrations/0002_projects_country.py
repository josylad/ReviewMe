# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-20 14:39
from __future__ import unicode_literals

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('awwards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='country',
            field=django_countries.fields.CountryField(default='NG', max_length=2),
        ),
    ]
