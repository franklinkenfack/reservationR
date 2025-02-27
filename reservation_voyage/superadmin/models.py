from django.db import models
from all_admin.models import AllAdmin  # Importer le modèle AllAdmin

class SuperAdmin(models.Model):
     # Énumération pour l'état du voyage (state)
    STATE_CHOICES = [
        ('VISIBLE', 'Visible'),  # Le voyage est visible
        ('DELETE', 'Delete'),    # Le voyage est supprimé (masqué)
    ]
    
    superadmin_id = models.AutoField(primary_key=True)  # ID unique pour chaque SuperAdmin
    rank = models.PositiveIntegerField(default=1, help_text="Niveau hiérarchique de l'admin")  # Attribut pour définir le niveau d'importance
    all_admin = models.ForeignKey(AllAdmin, on_delete=models.CASCADE,  null=True)  # Clé étrangère vers AllAdmin
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='VISIBLE')  # Champ state ajouté

    class Meta:
        verbose_name = 'SuperAdmin'
        verbose_name_plural = 'SuperAdmins'

    def __str__(self):
        return f"SuperAdmin {self.superadmin_id}"