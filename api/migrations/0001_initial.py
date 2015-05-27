# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wuser',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('email', models.TextField(null=True, blank=True)),
                ('name', models.TextField(null=True, blank=True)),
                ('display_name', models.TextField(null=True, blank=True)),
                ('current_country', models.TextField(null=True, blank=True)),
                ('current_city', models.TextField(null=True, blank=True)),
                ('gender', models.CharField(max_length=1, null=True, blank=True)),
                ('date_of_birth', models.CharField(max_length=10, null=True, blank=True)),
                ('college_country', models.TextField(null=True, blank=True)),
                ('college_name', models.TextField(null=True, blank=True)),
                ('sign_up_type', models.CharField(max_length=1, null=True, blank=True)),
                ('is_reported_abuse', models.NullBooleanField()),
                ('last_login', models.DateTimeField(null=True, blank=True)),
                ('time_created', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'wuser',
                'managed': False,
            },
        ),
    ]
