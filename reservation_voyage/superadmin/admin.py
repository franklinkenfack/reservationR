from django.contrib import admin
from .models import SuperAdmin  # Importation du modèle SuperAdmin

class SuperAdminAdmin(admin.ModelAdmin):
    # Liste des champs à afficher dans l'interface d'administration
    list_display = ('superadmin_id', 'rank', 'all_admin')  # Afficher l'ID, le rank et la clé étrangère vers AllAdmin
    # Ajouter un filtre pour faciliter la navigation
    list_filter = ('rank', 'all_admin')  # Filtrer par rank et all_admin
    # Ajouter une barre de recherche (optionnel)
    search_fields = ('superadmin_id',)  # Rechercher par superadmin_id
    
# Enregistrement du modèle SuperAdmin avec sa classe d'administration personnalisée
admin.site.register(SuperAdmin, SuperAdminAdmin)