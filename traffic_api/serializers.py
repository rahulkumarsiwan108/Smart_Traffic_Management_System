from rest_framework import serializers
from .models import Vehicle, TrafficData

# ✅ Vehicle Serializer
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

# ✅ Traffic Data Serializer
class TrafficDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficData
        fields = '__all__'
