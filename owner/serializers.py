from rest_framework import serializers
from .models import HostelOwner

class HostelOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HostelOwner
        fields = '__all__'