# Generated by Django 4.1.5 on 2023-02-07 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0006_car_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=1)),
                ('date', models.DateField(auto_now_add=True)),
                ('credit_card', models.IntegerField(blank=True, max_length=16, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='market.order')),
            ],
        ),
    ]
