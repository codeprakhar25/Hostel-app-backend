
from rest_framework.routers import DefaultRouter
from .views import TenantViewSet, RentViewSet, AttachmentViewSet

router = DefaultRouter()
router.register(r'tenants', TenantViewSet)
router.register(r'rents', RentViewSet)
router.register(r'attachments', AttachmentViewSet)

urlpatterns = router.urls
