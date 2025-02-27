from django.db import models

class CityCrossLine(models.Model):
    # Énumération pour l'état du voyage (state)
    STATE_CHOICES = [
        ('VISIBLE', 'Visible'),  # Le voyage est visible
        ('DELETE', 'Delete'),    # Le voyage est supprimé (masqué)
    ]

    city_id = models.AutoField(primary_key=True)  # Auto-incrémenté
    country = models.CharField(max_length=100)  # Pays de la ville
    city_name = models.CharField(max_length=100)  # Nom de la ville
    line = models.CharField(max_length=255, null=True, blank=True)  # Champ texte au lieu de ForeignKey
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='VISIBLE')  # Champ state ajouté

    class Meta:
        verbose_name = 'CityCross'
        verbose_name_plural = 'CitiesCross'

    def __str__(self):
        return f"{self.city_name}, {self.country}"
