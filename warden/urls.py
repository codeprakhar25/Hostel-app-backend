# wardens/urls.py

from rest_framework.routers import DefaultRouter
from .views import WardenViewSet

router = DefaultRouter()
router.register(r'wardens', WardenViewSet)

urlpatterns = router.urls
