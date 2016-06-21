# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-20 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('genreId', models.AutoField(primary_key=True, serialize=False)),
                ('genreName', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('trackId', models.AutoField(primary_key=True, serialize=False)),
                ('trackTitle', models.CharField(max_length=20, unique=True)),
                ('trackRating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)])),
                ('trackGenre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Track.Genre')),
            ],
        ),
    ]