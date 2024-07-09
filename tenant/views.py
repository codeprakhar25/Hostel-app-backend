
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated

from backend.permissions import IsHostelOwnerOrWarden
from .models import Tenant, Rent, Attachment
from .serializers import TenantSerializer, RentSerializer, AttachmentSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone

class TenantViewSet(viewsets.ModelViewSet):
    queryset = Tenant.objects.all()
    serializer_class = TenantSerializer
    permission_classes=[IsHostelOwnerOrWarden]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['hostel', 'room', 'rent_frequency', 'phone_number','next_due_date']
    search_fields = ['name', 'aadhar_number','phone_number','next_due_date' ]
    ordering_fields = ['name', 'start_date', 'rent_amount']
    ordering = ['name']

    @action(detail=False, methods=['get'])
    def by_hostel(self, request, pk=None):
        hostel_id = request.query_params.get('hostel_id')
        if hostel_id:
            tenants = Tenant.objects.filter(hostel_id=hostel_id)
            serializer = self.get_serializer(tenants, many=True)
            return Response(serializer.data)
        return Response({"error": "hostel_id parameter is required."}, status=400)

    @action(detail=False, methods=['get'])
    def by_room(self, request, pk=None):
        room_id = request.query_params.get('room_id')
        if room_id:
            tenants = Tenant.objects.filter(room_id=room_id)
            serializer = self.get_serializer(tenants, many=True)
            return Response(serializer.data)
        return Response({"error": "room_id parameter is required."}, status=400)

    @action(detail=True, methods=['get'])
    def rents(self, request, pk=None):
        tenant = self.get_object()
        rents = Rent.objects.filter(tenant=tenant)
        serializer = RentSerializer(rents, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def attachments(self, request, pk=None):
        tenant = self.get_object()
        attachments = Attachment.objects.filter(tenant=tenant)
        serializer = AttachmentSerializer(attachments, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'], url_path='rent-pending-by-hostel')
    def rent_pending_by_hostel(self, request):
        hostel_id = request.query_params.get('hostel_id')
        if not hostel_id:
            return Response({"error": "hostel_id parameter is required."}, status=400)
        
        today = timezone.now().date()
        tenants = Tenant.objects.filter(
            hostel_id=hostel_id,
            rents__rent_due_date__lt=today,
            rents__rent_remaining__gt=0
        ).distinct()

        serializer = TenantSerializer(tenants, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='due-date-passed-by-hostel')
    def due_date_passed_by_hostel(self, request):
        hostel_id = request.query_params.get('hostel_id')
        if not hostel_id:
            return Response({"error": "hostel_id parameter is required."}, status=400)
        
        today = timezone.now().date()
        tenants = Tenant.objects.filter(
            hostel_id=hostel_id,
            next_due_date__lt=today
        )

        serializer = TenantSerializer(tenants, many=True)
        return Response(serializer.data)

class RentViewSet(viewsets.ModelViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer
    permission_classes=[IsHostelOwnerOrWarden]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['tenant', 'amount', 'date', 'rent_due_date']
    search_fields = ['tenant__name']
    ordering_fields = ['date', 'amount', 'rent_due_date']
    ordering = ['date']

class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes=[IsHostelOwnerOrWarden]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['tenant']
    search_fields = ['file_description']
    ordering_fields = ['id']
    ordering = ['id']
