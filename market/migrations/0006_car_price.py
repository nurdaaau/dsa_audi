# Generated by Django 4.1.5 on 2023-02-07 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0005_purchase_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
