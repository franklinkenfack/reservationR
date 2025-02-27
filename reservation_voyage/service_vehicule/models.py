from django.db import models

class ServiceAvailable(models.Model):
    wifi = models.BooleanField(default=False)  # Wifi disponible ou non
    electric_socket = models.BooleanField(default=False)  # Prises électriques disponibles ou non
    air_conditioning = models.BooleanField(default=False)  # Climatisation disponible ou non
    toilet = models.BooleanField(default=False)  # Toilettes disponibles ou non
    seatbelt = models.BooleanField(default=False)  # Ceintures de sécurité disponibles ou non
    entertainment_screen = models.BooleanField(default=False)  # Écrans de divertissement disponibles ou non

    class Meta:
        verbose_name = 'ServiceAvailable'
        verbose_name_plural = 'ServicesAvailable'

    def __str__(self):
        return f"Service ID: {self.id}"