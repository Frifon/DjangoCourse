# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-12 16:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160312_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materialmark',
            name='data',
            field=models.CharField(max_length=100),
        ),
    ]
