from django.db import models

class Agency(models.Model):
    # Énumération 
    STATE_CHOICES = [
        ('VISIBLE', 'Visible'),  
        ('DELETE', 'Delete'),   
    ]
    agency_id = models.AutoField(primary_key=True)
    agency_name = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    localite = models.CharField(max_length=100, blank=True, null=True)  # Ajout de la localité
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='VISIBLE')  # Champ state ajouté

    class Meta:
        verbose_name = 'Agency'
        verbose_name_plural = 'Agencies'

    def __str__(self):
        return f"{self.agency_name} - {self.localite}, {self.city}, {self.country}"

    def get_authorised_admins(self):
        """Retourne la liste des administrateurs autorisés pour cette agence."""
        return self.admins.all()
