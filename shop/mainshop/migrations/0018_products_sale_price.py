# Generated by Django 3.2.23 on 2023-11-20 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainshop', '0017_alter_products_cat'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='sale_price',
            field=models.IntegerField(default=0),
        ),
    ]
