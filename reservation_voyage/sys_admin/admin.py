from django.contrib import admin
from .models import SysAdmin  # Importation du modèle SysAdmin

class SysAdminAdmin(admin.ModelAdmin):
    # Liste des champs à afficher dans l'interface d'administration
    list_display = ('admin_id', 'all_admin','state')  # Afficher l'ID et la clé étrangère vers AllAdmin
    
admin.site.register(SysAdmin, SysAdminAdmin)