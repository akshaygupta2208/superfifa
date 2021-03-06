# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-25 18:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chairman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rating', models.IntegerField(default=0)),
                ('image_url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message1', models.TextField(blank=True, null=True)),
                ('message2', models.TextField(blank=True, null=True)),
                ('message3', models.TextField(blank=True, null=True)),
                ('message4', models.TextField(blank=True, null=True)),
                ('reply', models.TextField(blank=True, null=True)),
                ('option1', models.TextField(blank=True, null=True)),
                ('option2', models.TextField(blank=True, null=True)),
                ('option3', models.TextField(blank=True, null=True)),
                ('option4', models.TextField(blank=True, null=True)),
                ('type', models.CharField(blank=True, choices=[(b'P', b'PLAYER'), (b'C', b'CHAIRMAN'), (b'M', b'MANAGER')], max_length=2, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChatLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('actor', models.CharField(choices=[(b'Y', b'YOU'), (b'B', b'BOT')], max_length=2)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('chairman', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Chairman')),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(choices=[(b'M', b'MENTAL'), (b'P', b'PHYSICAL')], max_length=2)),
                ('reputation', models.IntegerField(default=0)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('flag_url', models.CharField(max_length=255)),
                ('image_url', models.CharField(max_length=255)),
                ('wage', models.IntegerField(default=0)),
                ('transfer_fee', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Journalist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('image_url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rating', models.IntegerField(default=0)),
                ('image_url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rating', models.IntegerField(default=0)),
                ('image_url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MediaCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('news_type', models.CharField(choices=[(b'G', b'GOOD'), (b'B', b'BAD')], max_length=2)),
                ('news_date', models.DateField(auto_now_add=True)),
                ('journalist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Journalist')),
            ],
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image_url', models.CharField(max_length=255)),
                ('purchase_cost', models.IntegerField(default=0)),
                ('running_cost', models.IntegerField(default=0)),
                ('player_capacity', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image_url', models.CharField(max_length=255)),
                ('age', models.IntegerField(default=0)),
                ('current_ability', models.IntegerField(default=0)),
                ('potential_ability', models.IntegerField(default=0)),
                ('overall_ability', models.IntegerField(default=0)),
                ('performance', models.IntegerField(default=0)),
                ('happiness', models.IntegerField(default=0)),
                ('agency', models.CharField(max_length=255)),
                ('current_contract', models.IntegerField(default=0)),
                ('value', models.IntegerField(default=0)),
                ('salary', models.IntegerField(default=0)),
                ('signing_fee', models.IntegerField(default=0)),
                ('bonus', models.IntegerField(default=0)),
                ('wins', models.IntegerField(default=0)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('flag_url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Scout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('rating', models.IntegerField(default=0)),
                ('image_url', models.CharField(max_length=255)),
                ('hiring_fee', models.IntegerField(default=0)),
                ('transfer_fee', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rating', models.IntegerField(default=0)),
                ('image_url', models.CharField(max_length=255)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('league', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.League')),
            ],
        ),
        migrations.CreateModel(
            name='UserCurrentTrack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_mental_coach', models.TextField(blank=True, null=True)),
                ('current_physical_coach', models.TextField(blank=True, null=True)),
                ('current_office', models.TextField(blank=True, null=True)),
                ('upagrade_office_list', models.TextField(blank=True, null=True)),
                ('current_scout_list', models.TextField(blank=True, null=True)),
                ('base_commission', models.TextField(blank=True, null=True)),
                ('transfer_commission', models.TextField(blank=True, null=True)),
                ('sponsiorship_commission', models.TextField(blank=True, null=True)),
                ('miscellanious_income', models.TextField(blank=True, null=True)),
                ('miscellanious_expences', models.TextField(blank=True, null=True)),
                ('staff_wage', models.TextField(blank=True, null=True)),
                ('scout_hire_time', models.TextField(blank=True, null=True)),
                ('scout_hire_duration', models.TextField(blank=True, null=True)),
                ('physical_coach_hire_time', models.TextField(blank=True, null=True)),
                ('physical_coach_hire_duration', models.TextField(blank=True, null=True)),
                ('mental_coach_hire_time', models.TextField(blank=True, null=True)),
                ('mental_coach_hire_duration', models.TextField(blank=True, null=True)),
                ('current_week', models.TextField(blank=True, null=True)),
                ('agency_reputation', models.TextField(blank=True, null=True)),
                ('news_feed', models.TextField(blank=True, null=True)),
                ('negotiations', models.TextField(blank=True, null=True)),
                ('journalist_interactions', models.TextField(blank=True, null=True)),
                ('mail_box', models.TextField(blank=True, null=True)),
                ('player_list', models.ManyToManyField(to='api.Player')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='current_club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Team'),
        ),
        migrations.AddField(
            model_name='player',
            name='interested_club',
            field=models.ManyToManyField(related_name='api_player_related', to='api.Team'),
        ),
        migrations.AddField(
            model_name='news',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Player'),
        ),
        migrations.AddField(
            model_name='manager',
            name='team',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Team'),
        ),
        migrations.AddField(
            model_name='journalist',
            name='company',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.MediaCompany'),
        ),
        migrations.AddField(
            model_name='chatlog',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Manager'),
        ),
        migrations.AddField(
            model_name='chatlog',
            name='player',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Player'),
        ),
        migrations.AddField(
            model_name='chatlog',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chairman',
            name='team',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Team'),
        ),
    ]
