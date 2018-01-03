# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-20 21:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('location', models.CharField(max_length=32)),
                ('connected', models.BooleanField(default=False)),
                ('current_module', models.CharField(choices=[('GAL', 'Gallery'), ('WEA', 'Weather'), ('CAL', 'Calendar'), ('VID', 'Video')], default='WEA', max_length=3)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
