# hostels/urls.py

from rest_framework.routers import DefaultRouter
from .views import HostelViewSet, HostelRoomViewSet

router = DefaultRouter()
router.register(r'hostels', HostelViewSet)
router.register(r'hostel-rooms', HostelRoomViewSet)

urlpatterns = router.urls
