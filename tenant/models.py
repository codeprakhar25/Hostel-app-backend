from django.db import models
from hostel.models import Hostel
from room.models import Room

RENT_FREQUENCY_CHOICES = [
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('fortnight', 'Fortnight'),
    ('monthly', 'Monthly'),
    ('bimonthly', 'Bimonthly'),
    ('quarterly', 'Quarterly'),
    ('half_yearly', 'Half-yearly'),
    ('yearly', 'Yearly'),
]

class Tenant(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, unique=True)
    hostel = models.ForeignKey(Hostel, on_delete=models.PROTECT)
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    start_date = models.DateField()
    aadhar_number = models.CharField(max_length=12, blank=True, null=True)
    pan_number = models.CharField(max_length=10, blank=True, null=True)
    father_name = models.CharField(max_length=255, blank=True, null=True)
    father_phone_number = models.CharField(max_length=15, blank=True, null=True)
    mother_name = models.CharField(max_length=255, blank=True, null=True)
    mother_phone_number = models.CharField(max_length=15, blank=True, null=True)
    rent_amount = models.IntegerField()
    deposit_amount = models.IntegerField(default=0)
    rent_frequency = models.CharField(max_length=20, choices=RENT_FREQUENCY_CHOICES)
    tenant_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Rent(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.PROTECT, related_name='rents')
    amount = models.IntegerField()
    date = models.DateField()
    electricity_amount=models.IntegerField(blank=True, null=True)
    water_amount= models.IntegerField(blank=True, null=True)
    rent_remaining = models.IntegerField(default=0)
    rent_due_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"Rent for {self.tenant.name} on {self.date}"

class Attachment(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.PROTECT, related_name='attachments')
    file = models.FileField(upload_to='attachments/')
    file_description = models.TextField()

    def __str__(self):
        return f"Attachment for {self.tenant.name}"
