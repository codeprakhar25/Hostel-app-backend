# hostels/urls.py

from rest_framework.routers import DefaultRouter
from .views import HostelViewSet

router = DefaultRouter()
router.register(r'hostels', HostelViewSet)

urlpatterns = router.urls
