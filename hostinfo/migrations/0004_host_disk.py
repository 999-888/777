# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 10:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('hostinfo', '0003_remove_host_disk'),
    ]

    operations = [
        migrations.AddField(
            model_name='host',
            name='disk',
            field=models.CharField(default=datetime.datetime(2016, 5, 27, 10, 21, 32, 448968, tzinfo=utc), max_length=50, verbose_name='\u78c1\u76d8\u7a7a\u95f4\u603b\u91cf'),
            preserve_default=False,
        ),
    ]
