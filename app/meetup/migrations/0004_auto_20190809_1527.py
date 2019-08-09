# Generated by Django 2.2.3 on 2019-08-09 15:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetup', '0003_auto_20190806_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='rating',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AlterField(
            model_name='eventreview',
            name='rating',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
