# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-29 12:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streamapp', '0005_auto_20190329_1235'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BlogCategory',
            new_name='BlogCategorie',
        ),
        migrations.AlterModelTable(
            name='blogcategorie',
            table=None,
        ),
    ]
