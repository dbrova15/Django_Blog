# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Spalah_Django', '0003_auto_20170830_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(default=None, upload_to='img/'),
        ),
    ]
