# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-01 16:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fincomm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='transaction',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='fincomm.Account'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='debtor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='debtor', to='fincomm.Account'),
        ),
    ]