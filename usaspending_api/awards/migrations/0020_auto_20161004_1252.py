# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0019_auto_20161004_1236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='award',
            old_name='period_of_performance_star',
            new_name='period_of_performance_current_end_date',
        ),
        migrations.AddField(
            model_name='award',
            name='period_of_performance_start_date',
            field=models.DateField(null=True),
        ),
    ]
