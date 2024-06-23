# hostels/serializers.py

from rest_framework import serializers

from authentication.models import CustomUser
from backend import settings
from hostel.models import Hostel

class HostelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hostel
        fields = '__all__'


