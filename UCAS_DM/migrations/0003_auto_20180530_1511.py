# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-30 07:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UCAS_DM', '0002_auto_20180529_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='opinion_leader',
            field=models.CharField(default='-', max_length=100, verbose_name='\u9886\u5bfc\u610f\u89c1'),
        ),
    ]
