# Generated by Django 4.2.16 on 2025-01-12 05:14

import django.core.validators
from django.db import migrations, models
import localflavor.in_.models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0002_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='state',
            field=localflavor.in_.models.INStateField(default='KL', max_length=2),
        ),
        migrations.AddField(
            model_name='location',
            name='zipcode',
            field=models.CharField(blank=True, help_text='Enter a valid 6-digit Indian postal code.', max_length=6, validators=[django.core.validators.RegexValidator(message='Enter a valid 6-digit ZIP code.', regex='^\\d{6}$')]),
        ),
        migrations.AlterField(
            model_name='location',
            name='address1',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
