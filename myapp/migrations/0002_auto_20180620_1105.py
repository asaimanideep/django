# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-20 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='mobile_num',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='zipcode',
            field=models.IntegerField(),
        ),
    ]
