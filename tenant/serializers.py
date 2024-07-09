
from rest_framework import serializers

from hostel.serializers import HostelSerializer
from room.serializers import RoomSerializer
from .models import Tenant, Rent, Attachment


class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = '__all__'

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'

class TenantSerializer(serializers.ModelSerializer):
    rents = RentSerializer(many=True, read_only=True)
    room = RoomSerializer(many=False, read_only=True)
    hostel = HostelSerializer(many=False, read_only=True)
    attachments = AttachmentSerializer(many=True, read_only=True)
    class Meta:
        model = Tenant
        fields = '__all__'

    def create(self, validated_data):
        hostel_data = self.initial_data.get('hostel')
        room_data = self.initial_data.get('room')
        
        if not hostel_data or not room_data:
            raise serializers.ValidationError({"hostel": "Hostel and room fields are required."})

        validated_data['hostel_id'] = hostel_data
        validated_data['room_id'] = room_data

        return super().create(validated_data)