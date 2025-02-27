from django.contrib import admin
from .models import LogAdmin  # Importer le modèle LogAdmin

class LogAdminAdmin(admin.ModelAdmin):
    # Liste des champs à afficher dans l'interface d'administration
    list_display = ('log_id', 'all_admin', 'all_admin_some_id', 'driver_id', 'vehicle_id', 'agency_id', 'trip_id', 'date_added')

# Enregistrement du modèle LogAdmin avec sa classe d'administration personnalisée
admin.site.register(LogAdmin, LogAdminAdmin)