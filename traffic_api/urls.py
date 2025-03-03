from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, TrafficDataListCreate  # ✅ Import fix

# ✅ Router setup
router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet)  # /api/vehicles/

urlpatterns = [
    path('traffic/', TrafficDataListCreate.as_view(), name='traffic-list-create'),
    path('', include(router.urls)),  # ✅ Vehicles API included
]
