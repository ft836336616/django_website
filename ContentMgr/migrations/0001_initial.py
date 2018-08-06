# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-08-06 07:29
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from ..models import codec_tbls_construct


def create_constant_tables(apps, schema_editor):
    codec_tbls_construct()


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AAA', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='EnvironmentCodec',
            fields=[
                ('id', models.IntegerField(choices=[(1, 'QUIET'), (2, 'RESTRERANT'), (3, 'INDOOR'), (4, 'OUTDOOR')], primary_key=True, serialize=False)),
                ('enviro_type', models.CharField(editable=False, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='EventTypeCodec',
            fields=[
                ('id', models.IntegerField(choices=[(1, 'POWER_ON'), (2, 'POWER_OFF'), (3, 'MAP_SWITCH'), (4, 'INPUT_SEL_SWITCH'), (5, 'MODE_SWITCH')], primary_key=True, serialize=False)),
                ('event_type', models.CharField(editable=False, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='InputSelCodec',
            fields=[
                ('id', models.IntegerField(choices=[(1, 'MIC'), (2, 'T-COIL'), (3, 'AUX_IN'), (4, 'MIC_T-COIL'), (5, 'MIC_AUX_IN')], primary_key=True, serialize=False)),
                ('input_sel', models.CharField(editable=False, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Logging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('volume', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(12)])),
                ('battery', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ContentMgr.EnvironmentCodec')),
                ('input_sel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ContentMgr.InputSelCodec')),
            ],
        ),
        migrations.CreateModel(
            name='LoggingEnvironmentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='LoggingEnvironmentTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_time', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LoggingInputSelDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='LoggingInputSelTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_time', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LoggingMapDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='LoggingMapTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_time', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LoggingModeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='LoggingModeTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_time', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LoggingPowerOnDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='LoggingPowerOnTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(unique=True)),
                ('total_time', models.PositiveIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoggingPowerOnTime', to='AAA.user_ext')),
            ],
        ),
        migrations.CreateModel(
            name='MapCodec',
            fields=[
                ('id', models.IntegerField(choices=[(1, 'MAP1'), (2, 'MAP2'), (3, 'MAP3'), (4, 'MAP4')], primary_key=True, serialize=False)),
                ('map', models.CharField(editable=False, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ModeCodec',
            fields=[
                ('id', models.IntegerField(choices=[(1, 'RICH'), (2, 'NORMAL')], primary_key=True, serialize=False)),
                ('mode', models.CharField(editable=False, max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='loggingpowerondetails',
            name='date_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoggingPowerOnDetails', to='ContentMgr.LoggingPowerOnTime'),
        ),
        migrations.AddField(
            model_name='loggingmodetime',
            name='date_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoggingModeTime', to='ContentMgr.LoggingPowerOnTime'),
        ),
        migrations.AddField(
            model_name='loggingmodetime',
            name='mode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ContentMgr.ModeCodec'),
        ),
        migrations.AddField(
            model_name='loggingmodedetails',
            name='on_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoggingModeDetails', to='ContentMgr.LoggingModeTime'),
        ),
        migrations.AddField(
            model_name='loggingmaptime',
            name='date_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoggingMapTime', to='ContentMgr.LoggingPowerOnTime'),
        ),
        migrations.AddField(
            model_name='loggingmaptime',
            name='map',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ContentMgr.MapCodec'),
        ),
        migrations.AddField(
            model_name='loggingmapdetails',
            name='on_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoggingMapDetails', to='ContentMgr.LoggingMapTime'),
        ),
        migrations.AddField(
            model_name='logginginputseltime',
            name='date_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoggingInputSelTime', to='ContentMgr.LoggingPowerOnTime'),
        ),
        migrations.AddField(
            model_name='logginginputseltime',
            name='input_sel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ContentMgr.InputSelCodec'),
        ),
        migrations.AddField(
            model_name='logginginputseldetails',
            name='on_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoggingInputSelDetails', to='ContentMgr.LoggingInputSelTime'),
        ),
        migrations.AddField(
            model_name='loggingenvironmenttime',
            name='date_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoggingEnvironmentTime', to='ContentMgr.LoggingPowerOnTime'),
        ),
        migrations.AddField(
            model_name='loggingenvironmenttime',
            name='environment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ContentMgr.EnvironmentCodec'),
        ),
        migrations.AddField(
            model_name='loggingenvironmentdetails',
            name='on_time',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='LoggingEnvironmentDetails', to='ContentMgr.LoggingEnvironmentTime'),
        ),
        migrations.AddField(
            model_name='logging',
            name='map',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ContentMgr.MapCodec'),
        ),
        migrations.AddField(
            model_name='logging',
            name='mode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ContentMgr.ModeCodec'),
        ),
        migrations.AddField(
            model_name='logging',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Logging', to='AAA.user_ext'),
        ),

        migrations.RunPython(create_constant_tables),
    ]
