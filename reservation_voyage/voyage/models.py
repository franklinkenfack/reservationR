from django.db import models
from vehicule.models import Vehicle  # Importer le modèle Vehicle
from ligne.models import Line  # Importer le modèle Line

class Trip(models.Model):
    # Énumération pour le type de devise
    CURRENCY_CHOICES = [
        ('FCFA', 'FCFA'),
        ('DOLLAR', 'Dollar'),
        ('EURO', 'Euro'),
    ]
    
    # Énumération pour l'état du voyage (state)
    STATE_CHOICES = [
        ('VISIBLE', 'Visible'),  # Le voyage est visible
        ('DELETE', 'Delete'),    # Le voyage est supprimé (masqué)
    ]

    trip_id = models.AutoField(primary_key=True)
    departure_time = models.DateTimeField()
    approximate_arrival_time = models.DateTimeField()
    vehicule = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    line = models.ForeignKey(Line, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, choices=CURRENCY_CHOICES, default='FCFA')
    reduce_price_state = models.BooleanField(default=False)
    reduce_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='VISIBLE')  # Champ state ajouté

    class Meta:
        verbose_name = 'Trip'
        verbose_name_plural = 'Trips'

    def __str__(self):
        return f"Trip {self.trip_id}: {self.departure_time} -> {self.approximate_arrival_time}"