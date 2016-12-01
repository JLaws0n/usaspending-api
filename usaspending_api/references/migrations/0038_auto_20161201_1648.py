# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-12-01 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0037_auto_20161107_1218'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='location_state_description',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='State Description'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='cgac_code',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Agency Code'),
        ),
        migrations.AlterField(
            model_name='agency',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Agency Name'),
        ),
        migrations.RemoveField(
            model_name='location',
            name='location_state_text',
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together=set([('location_country_code', 'location_country_name', 'location_state_code', 'location_state_name', 'location_state_description', 'location_city_name', 'location_city_code', 'location_county_name', 'location_county_code', 'location_address_line1', 'location_address_line2', 'location_address_line3', 'location_foreign_location_description', 'location_zip4', 'location_congressional_code', 'location_performance_code', 'location_zip_last4', 'location_zip5', 'location_foreign_postal_code', 'location_foreign_province', 'location_foreign_city_name', 'reporting_period_start', 'reporting_period_end')]),
        ),
    ]
