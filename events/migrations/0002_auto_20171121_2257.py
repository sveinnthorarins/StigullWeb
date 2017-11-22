# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-21 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-starts'], 'verbose_name': 'Viðburður', 'verbose_name_plural': 'Viðburðir'},
        ),
        migrations.AlterModelOptions(
            name='eventregistration',
            options={'ordering': ['time_registered'], 'verbose_name': 'Skráning á viðburð', 'verbose_name_plural': 'Skráningar á viðburði'},
        ),
        migrations.AlterField(
            model_name='eventregistration',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event', verbose_name='Viðburður'),
        ),
    ]