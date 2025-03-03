from django.http import JsonResponse
from rest_framework import viewsets, generics
from .models import Vehicle, TrafficData

from .models import Vehicle, TrafficData
from .serializers import TrafficDataSerializer, VehicleSerializer

# ✅ Test API
def test_api(request):
    return JsonResponse({"message": "API is working"})

# ✅ TrafficData API (Create & List)
class TrafficDataListCreate(generics.ListCreateAPIView):
    queryset = TrafficData.objects.all()
    serializer_class = TrafficDataSerializer

# ✅ Vehicle API (CRUD)
class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
