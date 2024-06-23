# hostels/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from backend.permissions import  IsHostelOwner, IsHostelOwnerOrWarden, IsWarden
from .models import Hostel
from .serializers import HostelSerializer

class HostelViewSet(viewsets.ModelViewSet):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer
    permission_classes = [IsHostelOwnerOrWarden]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'hostelowner'):
            return Hostel.objects.filter(owner=user.hostelowner)
        elif hasattr(user, 'warden'):
            return Hostel.objects.filter(warden=user.warden)
        else:
            return Hostel.objects.none()

