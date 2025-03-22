from django.contrib import admin

# Register your models here.
from .models import Stations,Vehicle,Rides,Customer

admin.site.register(Stations)
admin.site.register(Vehicle)
admin.site.register(Rides)
admin.site.register(Customer)