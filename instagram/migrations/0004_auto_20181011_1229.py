# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-11 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_auto_20181009_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(max_length=144),
        ),
    ]