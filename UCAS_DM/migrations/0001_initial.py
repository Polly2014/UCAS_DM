# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-29 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('document_id', models.AutoField(primary_key=True, serialize=False, verbose_name='\u6587\u6863ID')),
                ('location_from', models.CharField(max_length=50, verbose_name='\u6765\u6587\u5355\u4f4d')),
                ('valid_code', models.CharField(max_length=20, verbose_name='\u6587\u6863\u67e5\u9a8c\u7801')),
                ('document_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='\u6587\u6863\u6761\u7801\u53f7')),
                ('title', models.CharField(max_length=200, verbose_name='\u6807\u9898\u6458\u8981')),
                ('time_recieve', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u5f55\u5165\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u516c\u6587\u6587\u6863\u4fe1\u606f',
                'verbose_name_plural': '\u516c\u6587\u6587\u6863\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_forward', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u8f6c\u53d1\u65f6\u95f4')),
                ('location_to', models.CharField(max_length=50, verbose_name='\u8f6c\u53d1\u53bb\u5411')),
                ('time_recycle', models.DateTimeField(blank=True, null=True, verbose_name='\u56de\u6536\u65f6\u95f4')),
                ('opinion_leader', models.CharField(max_length=100, verbose_name='\u9886\u5bfc\u610f\u89c1')),
                ('document_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DocumentInfo', to='UCAS_DM.Document', verbose_name='\u6587\u6863\u4fe1\u606f')),
            ],
            options={
                'verbose_name': '\u516c\u6587\u6d41\u8f6c\u4fe1\u606f',
                'verbose_name_plural': '\u516c\u6587\u6d41\u8f6c\u4fe1\u606f',
            },
        ),
    ]
