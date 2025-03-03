from django.db import models

# ✅ Vehicle Model
class Vehicle(models.Model):
    number_plate = models.CharField(max_length=20, unique=True)
    vehicle_type = models.CharField(max_length=50)
    entry_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.number_plate

# ✅ Traffic Data Model
class TrafficData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100)
    vehicle_count = models.IntegerField()

    def __str__(self):
        return f"{self.location} - {self.timestamp}"
