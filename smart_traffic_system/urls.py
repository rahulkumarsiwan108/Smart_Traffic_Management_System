from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from traffic_monitoring.views import home_view

def api_root(request):
    return JsonResponse({
        "traffic_api": "/api/traffic/",
        "monitoring_api": "/api/monitoring/",
        "vehicles_api": "/api/traffic/vehicles/",  # ✅ Vehicles API path corrected
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root),  # ✅ API root endpoint
    path('api/traffic/', include('traffic_api.urls')),  # ✅ Traffic API
    path('api/monitoring/', include('traffic_monitoring.urls')),  # ✅ Monitoring API
    path('', home_view, name='home'),  # ✅ Home Route
]
