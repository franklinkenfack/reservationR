from django.contrib import admin
from .models import Trip

class TripAdmin(admin.ModelAdmin):
    list_display = ('trip_id', 'departure_time', 'approximate_arrival_time', 'vehicule', 'line', 'price', 'currency', 'reduce_price_state', 'reduce_price','state')

admin.site.register(Trip, TripAdmin)