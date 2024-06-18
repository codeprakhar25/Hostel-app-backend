# from django.db import models

# class Tenant(models.Model):
#     # Tenant details
#     tenant_name = models.CharField(max_length=255, blank=True, null=True)
#     tenant_contact_number = models.CharField(max_length=15, blank=True, null=True)
#     tenant_document_number = models.CharField(max_length=100, blank=True, null=True)
    
#     # Guardian details
#     guardian_name = models.CharField(max_length=255, blank=True, null=True)
#     guardian_contact_number = models.CharField(max_length=15, blank=True, null=True)
    
#     # Rent details
#     rent_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     room_number = models.CharField(max_length=50, blank=True, null=True)
#     bed_number = models.CharField(max_length=50, blank=True, null=True)
#     deposit_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
#     # Electricity details
#     electricity_reading = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
#     price_per_unit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
#     # Assets details
#     asset_name = models.CharField(max_length=255, blank=True, null=True)
#     asset_unit = models.CharField(max_length=50, blank=True, null=True)

#     def __str__(self):
#         return self.tenant_name if self.tenant_name else "Tenant"

#     class Meta:
#         verbose_name = 'Tenant'
#         verbose_name_plural = 'Tenants'