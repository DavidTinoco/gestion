# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-03-08 20:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('convivencia', '0007_auto_20170401_2306'),
    ]

    operations = [
        migrations.AddField(
            model_name='sanciones',
            name='NoExpulsion',
            field=models.BooleanField(default=False),
        ),
    ]
