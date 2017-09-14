# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 06:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('uid', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('caption', models.CharField(max_length=32, unique=True)),
                ('time', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cmdb.UserGroup'),
        ),
    ]
