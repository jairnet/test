# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-07 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('EC', 'Electronic'), ('HM', 'Home'), ('BK', 'Book'), ('Cl', 'Clohing'), ('TY', 'Toys')], max_length=50)),
                ('vendor', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('taxe', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.ImageField(upload_to='portadas')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Products',
                'ordering': ['name'],
            },
        ),
    ]
