from django.db import models

class Driver(models.Model):
    # Énumération pour l'état du voyage (state)
    STATE_CHOICES = [
        ('VISIBLE', 'Visible'),  # Le voyage est visible
        ('DELETE', 'Delete'),    # Le voyage est supprimé (masqué)
    ]

    driver_id = models.AutoField(primary_key=True)  # Auto-incrémenté
    driver_name = models.CharField(max_length=100)  # Nom du conducteur
    country_calling_code = models.CharField(max_length=5, blank=True, null=True)  # Code téléphonique du pays
    Tel_number = models.CharField(max_length=15)    # Numéro de téléphone
    country = models.CharField(max_length=100, blank=True, null=True)  # Pays du conducteur
    city = models.CharField(max_length=100, blank=True, null=True)     # Ville du conducteur
    localite = models.CharField(max_length=100, blank=True, null=True) # Localité du conducteur
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='VISIBLE')  # Champ state ajouté

    class Meta:
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'

    def __str__(self):
        return self.driver_name
