from django.contrib import admin
from .models import Authorisation

class AuthorisationAdmin(admin.ModelAdmin):
    list_display = ('authorisation_id', 'sys_admin', 'agency')  # Champs valides
    list_display_links = ('authorisation_id',)  # Rendre cliquable uniquement l'ID
    # search_fields = ('sys_admin__all_admin__admin_name', 'agency__name')  # Champs de recherche
    # list_filter = ('sys_admin', 'agency')  # Ajoute ces filtres si nécessaire

admin.site.register(Authorisation, AuthorisationAdmin)
