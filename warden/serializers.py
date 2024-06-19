# wardens/serializers.py

from rest_framework import serializers
from .models import Warden

class WardenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warden
        fields = '__all__'
