# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-25 18:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chairman',
            name='country',
        ),
        migrations.RemoveField(
            model_name='player',
            name='Potential_ability',
        ),
        migrations.RemoveField(
            model_name='player',
            name='bonus',
        ),
        migrations.RemoveField(
            model_name='player',
            name='wins',
        ),
        migrations.AddField(
            model_name='coach',
            name='transfer_fee',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='news',
            name='news_date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='potential_ability',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='player',
            name='salary',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='scout',
            name='transfer_fee',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='chairman',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coach',
            name='reputation',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='coach',
            name='wage',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='league',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_type',
            field=models.CharField(choices=[(b'G', b'GOOD'), (b'B', b'BAD')], max_length=2),
        ),
        migrations.AlterField(
            model_name='office',
            name='level',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='office',
            name='player_capacity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='office',
            name='purchase_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='office',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='office',
            name='running_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='current_ability',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='current_contract',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='happiness',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='overall_ability',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='performance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='value',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='scout',
            name='hiring_fee',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='scout',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='team',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]