# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostIp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr', models.CharField(max_length=50, verbose_name='IP\u5730\u5740')),
            ],
            options={
                'verbose_name': '\u670d\u52a1\u5668IP',
                'verbose_name_plural': '\u670d\u52a1\u5668IP',
            },
        ),
        migrations.AlterModelOptions(
            name='host',
            options={'verbose_name': '\u670d\u52a1\u5668', 'verbose_name_plural': '\u670d\u52a1\u5668'},
        ),
    ]
