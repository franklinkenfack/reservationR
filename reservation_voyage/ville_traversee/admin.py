from django.contrib import admin
from .models import CityCrossLine  # Importation du modèle

class CityCrossLineAdmin(admin.ModelAdmin):
    list_display = ('city_id', 'country', 'city_name', 'line','state')  # Ajout de city_id

admin.site.register( CityCrossLine,  CityCrossLineAdmin)