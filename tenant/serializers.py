
from rest_framework import serializers
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
    attachments = AttachmentSerializer(many=True, read_only=True)
    class Meta:
        model = Tenant
        fields = '__all__'