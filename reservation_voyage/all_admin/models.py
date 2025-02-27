from django.db import models
from django.contrib.auth.hashers import make_password

class AllAdmin(models.Model):
    # Énumération pour l'état du voyage (state)
    STATE_CHOICES = [
        ('VISIBLE', 'Visible'),  
        ('DELETE', 'Delete'),    
    ]
    admin_id = models.AutoField(primary_key=True)  # ID unique pour chaque Admin
    admin_name = models.CharField(max_length=150, blank=True, null=True)    # Nom de l'Admin
    country_calling_code = models.CharField(max_length=5, blank=True, null=True)  # Code téléphonique du pays
    tel_number = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=100, blank=True, null=True)  # Permet les valeurs nulles
    city = models.CharField(max_length=100, blank=True, null=True)  # Permet les valeurs nulles
    localite = models.CharField(max_length=100, blank=True, null=True) # Localité du conducteur
    mail = models.EmailField(null=True, blank=True)  # Permet les valeurs nulles
    password = models.CharField(max_length=128, blank=True, null=True, default=make_password('123456789'))  # Champ password ajouté avec valeur par défaut
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='VISIBLE')  # Champ state ajouté

    class Meta:
        verbose_name = 'AllAdmin'
        verbose_name_plural = 'AllAdmins'

    def __str__(self):
        return self.admin_name
