# Generated by Django 5.1.7 on 2025-03-22 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EV', '0003_customer_customer_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stations',
            name='station_vehicleId',
        ),
        migrations.AddField(
            model_name='stations',
            name='station_vehicles',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
