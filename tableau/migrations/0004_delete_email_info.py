# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-24 11:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tableau', '0003_remove_image_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='email_info',
        ),
    ]
