# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-06 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0012_image_image_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='user',
        ),
        migrations.AddField(
            model_name='image',
            name='profile',
            field=models.TextField(blank=True, max_length=50),
        ),
    ]
