# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-03 13:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(upload_to='home')),
                ('bio', models.TextField(max_length=144)),
            ],
        ),
    ]
