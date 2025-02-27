from django.db import models
from ville_traversee.models import CityCrossLine  # Importer le modèle CityCross

class Line(models.Model):
     # Énumération pour l'état du voyage (state)
    STATE_CHOICES = [
        ('VISIBLE', 'Visible'),  # Le voyage est visible
        ('DELETE', 'Delete'),    # Le voyage est supprimé (masqué)
    ]
    
    line_id = models.AutoField(primary_key=True)  # Auto-incrémenté
    starting_point = models.ForeignKey(CityCrossLine, on_delete=models.CASCADE, related_name='starting_lines')  # Point de départ
    arrival_location = models.ForeignKey(CityCrossLine, on_delete=models.CASCADE, related_name='arrival_lines')  # Point d'arrivée
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='VISIBLE')  # Champ state ajouté

    class Meta:
        verbose_name = 'Line'
        verbose_name_plural = 'Lines'

    def __str__(self):
        return f"Line {self.line_id}: {self.starting_point.city_name} -> {self.arrival_location.city_name}"