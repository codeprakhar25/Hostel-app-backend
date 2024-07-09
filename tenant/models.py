from django.db import models
from hostel.models import Hostel
from room.models import Room
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

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
    next_due_date = models.DateField(null=True)
    left_hostel = models.BooleanField(default=False)
    rent_frequency = models.CharField(max_length=20, choices=RENT_FREQUENCY_CHOICES)
    tenant_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    def has_rent_pending(self):
        most_recent_rent = self.rents.order_by('-rent_due_date').first()
        if most_recent_rent and most_recent_rent.rent_due_date and most_recent_rent.rent_due_date < datetime.now().date():
            return True
        return False

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
    
    def save(self, *args, **kwargs):
        super(Rent, self).save(*args, **kwargs)

        next_due_date = None
        current_date = datetime.today().date()

        if self.rent_due_date:
            current_date = self.rent_due_date

        if self.tenant.rent_frequency == 'daily':
            next_due_date = current_date + timedelta(days=1)
        elif self.tenant.rent_frequency == 'weekly':
            next_due_date = current_date + timedelta(weeks=1)
        elif self.tenant.rent_frequency == 'fortnight':
            next_due_date = current_date + timedelta(weeks=2)
        elif self.tenant.rent_frequency == 'monthly':
            next_due_date = current_date + relativedelta(months=1)
        elif self.tenant.rent_frequency == 'bimonthly':
            next_due_date = current_date + relativedelta(months=2)
        elif self.tenant.rent_frequency == 'quarterly':
            next_due_date = current_date + relativedelta(months=3)
        elif self.tenant.rent_frequency == 'half_yearly':
            next_due_date = current_date + relativedelta(months=6)
        elif self.tenant.rent_frequency == 'yearly':
            next_due_date = current_date + relativedelta(years=1)

        if next_due_date:
            self.tenant.next_due_date = next_due_date
            self.tenant.save(update_fields=['next_due_date'])


class Attachment(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.PROTECT, related_name='attachments')
    file = models.FileField(upload_to='attachments/')
    file_description = models.TextField()

    def __str__(self):
        return f"Attachment for {self.tenant.name}"
