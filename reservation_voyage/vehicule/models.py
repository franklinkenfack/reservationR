from django.db import models
from service_vehicule.models import ServiceAvailable  # Importer le modèle ServiceAvailable

class Vehicle(models.Model):
    # Types de véhicules (énumération)
    VEHICLE_TYPE_CHOICES = [
        ('BUS', 'Bus'),
        ('CAR', 'Car'),
        ('VAN', 'Van'),
        ('TRUCK', 'Truck'),
        ('MOTORCYCLE', 'Motorcycle'),
    ]
    # États du véhicule (énumération)
    VEHICLE_STATE_CHOICES = [
        ('USED', 'Used'),
        ('UNDER_MAINTENANCE', 'Under Maintenance'),
        ('OUT_OF_SERVICE', 'Out of Service'),
    ]
    
     # Énumération pour l'état du voyage (state)
    STATE_CHOICES = [
        ('VISIBLE', 'Visible'),  # Le voyage est visible
        ('DELETE', 'Delete'),    # Le voyage est supprimé (masqué)
    ]

    vehicule_id = models.AutoField(primary_key=True)  # Auto-incrémenté
    Vehicule_number = models.CharField(max_length=50, unique=True)  # Numéro du véhicule
    licence_plate = models.CharField(max_length=20, unique=True)  # Plaque d'immatriculation
    owner = models.CharField(max_length=100)  # Propriétaire du véhicule
    capacity = models.PositiveIntegerField()  # Capacité du véhicule (nombre de passagers)
    purchase_date = models.DateField()  # Date d'achat du véhicule
    vehicule_state = models.CharField(max_length=20, choices=VEHICLE_STATE_CHOICES)  # État du véhicule
    vehicule_type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)  # Type de véhicule
    service_available = models.ForeignKey(ServiceAvailable, on_delete=models.CASCADE)  # Clé étrangère vers ServiceAvailable
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default='VISIBLE')  # Champ state ajouté
    
    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

    def __str__(self):
        return f"{self.vehicule_type} - {self.Vehicule_number}"