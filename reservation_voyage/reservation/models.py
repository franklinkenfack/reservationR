from django.db import models
from voyage.models import Trip  # Importer le modèle Trip

class Reservation(models.Model):
    reservation_id = models.AutoField(primary_key=True)  # Auto-incrémenté
    customer_name = models.CharField(max_length=100)  # Nom du client
    CNI_number = models.CharField(max_length=20)  # Numéro de CNI
    Tel_number = models.CharField(max_length=15)  # Numéro de téléphone
    seat_number = models.PositiveIntegerField()  # Numéro de siège
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)  # Clé étrangère vers Trip

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return f"Reservation {self.reservation_id}: {self.customer_name} (Seat {self.seat_number})"