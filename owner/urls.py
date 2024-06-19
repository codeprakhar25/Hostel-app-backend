from rest_framework.routers import DefaultRouter
from .views import HostelOwnerViewSet

router = DefaultRouter()
router.register(r'owners', HostelOwnerViewSet)

urlpatterns = router.urls