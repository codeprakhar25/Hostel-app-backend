# rooms/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RoomViewSet

router = DefaultRouter()
router.register(r'rooms', RoomViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('hostels/<int:pk>/rooms/', RoomViewSet.as_view({'get': 'get_rooms_by_hostel'}), name='hostel-rooms'),
]
