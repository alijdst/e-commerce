# Generated by Django 3.2.23 on 2023-12-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainshop', '0006_auto_20231203_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='isbuy',
            name='is_buy',
            field=models.BooleanField(default=False),
        ),
    ]
