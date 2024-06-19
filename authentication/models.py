from django.contrib.auth.models import AbstractUser
from django.db import models


ROLE_CHOICES = [
        ('hostelowner', 'HostelOwner'),
        ('user', 'User'),
        ('warden', 'Warden'),
    ]

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255,blank=True,null=True)
    city = models.CharField(max_length=255,blank=True,null=True)
    role = models.CharField(max_length=100, choices=ROLE_CHOICES, default='user')
    contact_no = models.BigIntegerField(blank=True,null=True)
