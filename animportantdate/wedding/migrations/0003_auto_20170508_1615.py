# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-08 16:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0002_person_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='vanue',
            new_name='venue',
        ),
    ]
