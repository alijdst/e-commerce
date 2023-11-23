# Generated by Django 3.2.23 on 2023-11-21 01:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainshop', '0029_remove_products_star'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='star',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]