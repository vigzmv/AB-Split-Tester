# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-09 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testerhack', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersredirect',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
