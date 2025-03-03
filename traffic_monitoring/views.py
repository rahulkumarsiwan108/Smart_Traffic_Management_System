from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework import viewsets, generics
from .models import Vehicle, TrafficData

from .serializers import TrafficDataSerializer, VehicleSerializer


def test_api(request):
    return JsonResponse({"message": "API is working"})

# ✅ Home API
def home_view(request):
    return JsonResponse({"message": "Welcome to the Traffic Monitoring API!"})

# ✅ TrafficData API (Create & List)
@method_decorator(csrf_exempt, name='dispatch')
class TrafficDataListCreate(generics.ListCreateAPIView):
    queryset = TrafficData.objects.all()
    serializer_class = TrafficDataSerializer

# ✅ Vehicle API (CRUD)
class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
