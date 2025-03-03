from django.db import models

class Vehicle(models.Model):
    name = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=20, unique=True)

class TrafficData(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=255)
