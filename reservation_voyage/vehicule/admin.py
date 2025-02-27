from django.contrib import admin
from .models import Vehicle

class VehicleAdmin(admin.ModelAdmin):
    list_display = ('vehicule_id', 'Vehicule_number', 'licence_plate', 'owner', 'capacity', 'purchase_date', 'vehicule_state', 'vehicule_type', 'service_available', 'state')

admin.site.register(Vehicle, VehicleAdmin)