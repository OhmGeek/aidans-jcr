# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-16 12:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_peopledirectorypage_personprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='personprofile',
            name='description',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]