# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-01 20:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fincomm', '0002_auto_20180101_1650'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='creator',
        ),
    ]