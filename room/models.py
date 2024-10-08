from django.db import models

from hostel.models import Hostel

class Room(models.Model):
    room_number = models.CharField(max_length=10)
    room_floor = models.IntegerField()
    room_occupancy = models.IntegerField()
    has_ac = models.BooleanField(default=False)
    has_attached_bathroom = models.BooleanField(default=False)
    hostel = models.ForeignKey(Hostel, on_delete=models.PROTECT, related_name='rooms')
    extra_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Room {self.room_number}"