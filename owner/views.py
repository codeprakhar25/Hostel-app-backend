from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import HostelOwner
from .serializers import HostelOwnerSerializer

class HostelOwnerViewSet(viewsets.ModelViewSet):
    queryset = HostelOwner.objects.all()
    serializer_class = HostelOwnerSerializer
    permission_classes = [IsAuthenticated]  # Ensure user is authenticated

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)