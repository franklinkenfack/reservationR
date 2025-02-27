from django.contrib import admin
from .models import AllAdmin  # Importation du modèle AllAdmin

class AllAdminAdmin(admin.ModelAdmin):
    # Liste des champs à afficher dans l'interface d'administration
    list_display = ('admin_id', 'admin_name','country_calling_code', 'tel_number', 'mail', 'country', 'city','localite','password' , 'state')

# Enregistrement du modèle AllAdmin avec sa classe d'administration personnalisée
admin.site.register(AllAdmin, AllAdminAdmin)