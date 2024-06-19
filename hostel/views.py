# hostels/views.py

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Hostel, HostelRoom
from .serializers import HostelSerializer, HostelRoomSerializer

class HostelViewSet(viewsets.ModelViewSet):
    queryset = Hostel.objects.all()
    serializer_class = HostelSerializer
    permission_classes = [IsAuthenticated]

class HostelRoomViewSet(viewsets.ModelViewSet):
    queryset = HostelRoom.objects.all()
    serializer_class = HostelRoomSerializer
    permission_classes = [IsAuthenticated]
