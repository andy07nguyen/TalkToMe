# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 00:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talktome', '0007_auto_20170302_0158'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='roomname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
