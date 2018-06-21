# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-06-19 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('mobile_num', models.IntegerField(max_length=10)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('zipcode', models.IntegerField(max_length=6)),
            ],
        ),
    ]
