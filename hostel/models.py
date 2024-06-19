from django.db import models
from owner.models import HostelOwner
from warden.models import Warden
from room.models import Room

class Hostel(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    owner = models.ForeignKey(HostelOwner, on_delete=models.PROTECT)
    warden = models.OneToOneField(Warden, on_delete=models.PROTECT)
    extra_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class HostelRoom(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.PROTECT, related_name='rooms')
    room = models.ForeignKey(Room, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.hostel.name} - {self.room.room_number}"