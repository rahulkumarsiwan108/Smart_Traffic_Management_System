from django.urls import path
from .views import TrafficDataListCreate

urlpatterns = [
    path('data/', TrafficDataListCreate.as_view(), name='traffic-data-list-create'),
]
