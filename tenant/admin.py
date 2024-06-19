from django.contrib import admin
from .models import Rent,Tenant,Attachment

# Register your models here.
admin.site.register(Rent)
admin.site.register(Tenant)
admin.site.register(Attachment)
