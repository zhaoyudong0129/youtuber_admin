# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-12-05 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('influencer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='influencer',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='influencer',
            name='register_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='influencer',
            name='subscriber_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='influencer',
            name='view_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]