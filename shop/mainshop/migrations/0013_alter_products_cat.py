# Generated by Django 3.2.23 on 2023-11-16 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainshop', '0012_alter_products_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='cat',
            field=models.CharField(choices=[('arayeshi', 'arayeshi'), ('خوراکی', 'خوارکی'), ('پوشاک', 'پوشاک')], default='arayeshi', max_length=20),
        ),
    ]