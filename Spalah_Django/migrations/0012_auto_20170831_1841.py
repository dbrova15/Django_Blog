# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Spalah_Django', '0011_auto_20170831_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.FileField(upload_to='img/'),
        ),
    ]