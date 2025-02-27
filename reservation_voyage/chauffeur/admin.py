from django.contrib import admin
from .models import Driver

class DriverAdmin(admin.ModelAdmin):
    list_display = ('driver_id', 'driver_name','country_calling_code', 'Tel_number', 'country', 'city', 'localite', 'state')  # Colonnes affichées dans l'admin

admin.site.register(Driver, DriverAdmin)