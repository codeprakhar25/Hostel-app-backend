from django.db import models
from backend import settings

class HostelOwner(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    extra_info = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username
