# Generated by Django 3.2.23 on 2023-12-03 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainshop', '0005_products_buyer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='products',
            name='is_buy',
        ),
    ]