# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 14:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('benny', '0002_auto_20161124_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='account_type',
            new_name='accountType',
        ),
    ]
