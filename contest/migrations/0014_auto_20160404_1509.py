# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-04 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0013_auto_20151017_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestproblem',
            name='spj',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contestproblem',
            name='spj_code',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contestproblem',
            name='spj_code_language',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
