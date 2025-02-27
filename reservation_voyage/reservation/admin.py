from django.contrib import admin
from .models import Reservation

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('reservation_id', 'customer_name', 'CNI_number', 'Tel_number', 'seat_number', 'trip')  # Colonnes affichées dans l'admin

admin.site.register(Reservation, ReservationAdmin)