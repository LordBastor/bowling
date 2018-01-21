# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-21 15:26
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('bowling_game', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bowlinggame',
            name='rolls',
            field=models.CharField(blank=True, default='', max_length=511, null=True, validators=[django.core.validators.RegexValidator(re.compile('^\\d+(?:\\,\\d+)*\\Z', 32), code='invalid', message='Enter only digits separated by commas.')]),
        ),
    ]
