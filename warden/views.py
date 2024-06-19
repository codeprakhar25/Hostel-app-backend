# wardens/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Warden
from .serializers import WardenSerializer

class WardenViewSet(viewsets.ModelViewSet):
    queryset = Warden.objects.all()
    serializer_class = WardenSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
