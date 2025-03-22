from django.db import models

class Vehicle(models.Model):
    vehicle_id = models.AutoField(primary_key=True)  # Explicit primary key
    vehicle_model = models.CharField(max_length=100)
    vehicle_img = models.ImageField(upload_to="media/vehicle_images")
    vehicle_category = models.CharField(max_length=100)
    vehicle_status = models.BooleanField()
    vehicle_pricePerKm = models.PositiveIntegerField()
    vehicle_battery=models.PositiveIntegerField(null=True)
    vehicle_range = models.PositiveIntegerField()

class Stations(models.Model):
    station_id = models.AutoField(primary_key=True)
    station_location = models.CharField(max_length=100)
    station_master_name = models.CharField(max_length=100)
    station_availableVehicles = models.PositiveIntegerField()
    station_vehicles=models.CharField(max_length=100,null=True)

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)  # Explicit primary key
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_number=models.PositiveIntegerField(null=True)
    customer_password=models.CharField(max_length=100,null=True)
    customer_penalty=models.FloatField(null=True,default=0)

class Rides(models.Model):
    ride_id = models.AutoField(primary_key=True) 
    customer_id = models.CharField(max_length=100,null=True)  
    vehicle_id = models.CharField(max_length=100,null=True)
    pickup_station_id = models.CharField(max_length=100,null=True)
    drop_station_id = models.CharField(max_length=100,null=True)
    time = models.CharField(max_length=100, null=True, blank=True)
    distance = models.CharField(max_length=100, null=True, blank=True)
    total_cost = models.CharField(max_length=100, null=True, blank=True)
    damages = models.CharField(max_length=100, null=True, blank=True)
