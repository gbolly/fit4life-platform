# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-26 22:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='menu', to=settings.AUTH_USER_MODEL),
        ),
    ]