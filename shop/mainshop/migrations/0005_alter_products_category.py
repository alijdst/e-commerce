# Generated by Django 3.2.23 on 2023-11-15 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainshop', '0004_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category',
            field=models.CharField(choices=[('آرایشی بهداشتی', 'آرایشی-بهداشتی'), ('خوراکی', 'خوارکی'), ('پوشاک', 'پوشاک')], default='آرایشی بهداشتی', max_length=20),
        ),
    ]
