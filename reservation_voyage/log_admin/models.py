from django.db import models
from all_admin.models import AllAdmin  # Importer le modèle AllAdmin

class LogAdmin(models.Model):
    log_id = models.AutoField(primary_key=True)  # ID unique pour chaque log
    all_admin = models.ForeignKey(AllAdmin, on_delete=models.CASCADE)  # Clé étrangère vers AllAdmin (obligatoire)
    all_admin_some_id = models.CharField(max_length=100, blank=True, null=True)  # ID d'un autre admin (optionnel)
    driver_id = models.CharField(max_length=100, blank=True, null=True)  # ID du conducteur (optionnel)
    vehicle_id = models.CharField(max_length=100, blank=True, null=True)  # ID du véhicule (optionnel)
    agency_id = models.CharField(max_length=100, blank=True, null=True)  # ID de l'agence (optionnel)
    trip_id = models.CharField(max_length=100, blank=True, null=True)  # ID du voyage (optionnel)
    date_added = models.DateTimeField(auto_now_add=True)  # Date et heure d'ajout automatiques

    class Meta:
        verbose_name = 'LogAdmin'
        verbose_name_plural = 'LogAdmins'

    def __str__(self):
        return f"Log {self.log_id} - AllAdmin {self.all_admin.admin_name}"