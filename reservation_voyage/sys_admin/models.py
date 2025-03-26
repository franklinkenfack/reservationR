from django.db import models
from agence.models import Agency  # Importer le modèle Agency
from all_admin.models import AllAdmin  # Importer le modèle AllAdmin

class SysAdmin(models.Model):
     # Énumération pour l'état du voyage (state)
    STATE_CHOICES = [
        ('VISIBLE', 'Visible'),  # Le voyage est visible
        ('DELETE', 'Delete'),    # Le voyage est supprimé (masqué)
    ]
    
    admin_id = models.AutoField(primary_key=True)  # Auto-incrémenté
    all_admin = models.ForeignKey(AllAdmin, on_delete=models.CASCADE, null=True)  # Clé étrangère vers AllAdmin
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='VISIBLE')  # Champ state ajouté

    class Meta:
        verbose_name = 'SysAdmin'
        verbose_name_plural = 'SysAdmins'

    def __str__(self):
        return f"SysAdmin {self.admin_id}"