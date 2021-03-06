# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-06 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20160605_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Index', models.IntegerField(default=0)),
                ('Number', models.CharField(max_length=10)),
                ('Color', models.CharField(max_length=2)),
                ('Is_finded', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='Finded',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='Get_pos',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='Last_card',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='Num_of_joker',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='Turn',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='player',
            name='Hand',
            field=models.ManyToManyField(to='game.Card'),
        ),
        migrations.AddField(
            model_name='room',
            name='Deck',
            field=models.ManyToManyField(to='game.Card'),
        ),
    ]
