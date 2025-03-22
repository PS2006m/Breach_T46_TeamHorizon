# Generated by Django 5.1.7 on 2025-03-22 04:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('vehicle_id', models.AutoField(primary_key=True, serialize=False)),
                ('vehicle_model', models.CharField(max_length=100)),
                ('vehicle_img', models.ImageField(upload_to='media/vehicle_images')),
                ('vehicle_category', models.CharField(max_length=100)),
                ('vehicle_status', models.BooleanField()),
                ('vehicle_pricePerKm', models.PositiveIntegerField()),
                ('vehicle_range', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stations',
            fields=[
                ('station_id', models.AutoField(primary_key=True, serialize=False)),
                ('station_location', models.CharField(max_length=100)),
                ('station_master_name', models.CharField(max_length=100)),
                ('station_availableVehicles', models.PositiveIntegerField()),
                ('station_vehicleId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EV.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Rides',
            fields=[
                ('ride_id', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.CharField(blank=True, max_length=100, null=True)),
                ('distance', models.CharField(blank=True, max_length=100, null=True)),
                ('total_cost', models.CharField(blank=True, max_length=100, null=True)),
                ('damages', models.CharField(blank=True, max_length=100, null=True)),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EV.customer')),
                ('drop_station_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drop_rides', to='EV.stations')),
                ('pickup_station_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pickup_rides', to='EV.stations')),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EV.vehicle')),
            ],
        ),
    ]
