# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-07 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucketlist',
            name='price',
            field=models.IntegerField(default=2, unique=True),
            preserve_default=False,
        ),
    ]
