from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from backend.permissions import IsHostelOwnerOrWarden
from .models import Room
from .serializers import RoomSerializer
from hostel.models import Hostel

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['room_floor', 'room_occupancy']
    search_fields = ['^room_number', '^room_floor', '^room_occupancy']
    ordering_fields = ['room_number', 'room_floor', 'room_occupancy']
    serializer_class = RoomSerializer
    permission_classes = [IsHostelOwnerOrWarden]

    @action(detail=True, methods=['get'], url_path='rooms', permission_classes=[IsHostelOwnerOrWarden])
    def get_rooms_by_hostel(self, request, pk=None):
        try:
            hostel = Hostel.objects.get(pk=pk)
            rooms = Room.objects.filter(hostel=hostel)
            serializer = RoomSerializer(rooms, many=True)
            return Response(serializer.data)
        except Hostel.DoesNotExist:
            return Response({'error': 'Hostel not found'}, status=404)
