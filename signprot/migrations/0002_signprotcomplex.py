# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-09 19:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('protein', '0002_auto_20180117_1457'),
        ('structure', '0001_initial'),
        ('signprot', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignprotComplex',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chain', models.CharField(max_length=1)),
                ('protein', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='protein.Protein')),
                ('structure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.Structure')),
            ],
            options={
                'db_table': 'signprot_complex',
            },
        ),
    ]
