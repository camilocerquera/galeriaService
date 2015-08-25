# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=100)),
                ('msg', models.CharField(max_length=2048)),
                ('date', models.DateTimeField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.CharField(max_length=2048)),
                ('date', models.DateTimeField()),
                ('user', models.CharField(max_length=16)),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=2048)),
            ],
        ),
    ]
