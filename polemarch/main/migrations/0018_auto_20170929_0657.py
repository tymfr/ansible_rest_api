# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_periodictask_save_result'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='hosts',
            field=models.ManyToManyField(related_name='groups', related_query_name='groups', to='main.Host'),
        ),
    ]
