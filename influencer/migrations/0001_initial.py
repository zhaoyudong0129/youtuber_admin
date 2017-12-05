# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-12-05 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Influencer',
            fields=[
                ('object_url_id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200, null=True)),
                ('register_date', models.CharField(blank=True, max_length=200, null=True)),
                ('subscriber_count', models.CharField(blank=True, max_length=200, null=True)),
                ('view_count', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]