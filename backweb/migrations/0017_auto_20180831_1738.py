# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-31 09:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backweb', '0016_order_adderss'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='adderss',
            new_name='addersss',
        ),
    ]
