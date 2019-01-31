# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-01-31 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=255, unique=True)),
                ('street_name', models.CharField(max_length=255)),
                ('suburb', models.CharField(max_length=255)),
                ('postcode', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=255)),
                ('contact_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
    ]