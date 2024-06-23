from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


def limit_to_hostel_owners():
    return {'role': 'hostelowner'}

def limit_to_wardens():
    return {'role': 'warden'}


class Hostel(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    owners = models.ForeignKey(User,limit_choices_to= limit_to_hostel_owners, on_delete=models.PROTECT,related_name='owned_hostels')
    wardens = models.OneToOneField(User, limit_choices_to= limit_to_wardens, on_delete=models.PROTECT,related_name='warden_hostel')
    extra_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
