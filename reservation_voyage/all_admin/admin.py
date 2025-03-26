from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import AllAdmin

class AllAdminAdmin(UserAdmin):
    # Configuration de l'affichage de la liste
    list_display = (
        'admin_id',
        'admin_name',
        'mail',
        'country_calling_code',
        'tel_number',
        'country',
        'city',
        'localite',
        'admin_type',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    
    # Configuration des filtres
    list_filter = (
        'is_staff',
        'is_superuser',
        'is_active',
        'admin_type',
    )
    
    # Configuration des groupes de champs pour l'édition
    fieldsets = (
        (None, {'fields': ('mail', 'password')}),
        ('Informations personnelles', {
            'fields': (
                'admin_name',
                'country_calling_code',
                'tel_number',
                'country',
                'city',
                'localite',
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
        }),
        ('Type et état', {
            'fields': (
                'admin_type',
            ),
        }),
    )
    
    # Configuration des champs pour l'ajout d'un utilisateur
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'mail',
                'admin_name',
                'password1',
                'password2',
                'country_calling_code',
                'tel_number',
                'country',
                'city',
                'localite',
                'is_staff',
                'is_active',
            ),
        }),
    )
    
    # Configuration de la recherche
    search_fields = ('mail', 'admin_name', 'tel_number', 'city')
    ordering = ('admin_id',)
    filter_horizontal = ('groups', 'user_permissions',)

# Enregistrement du modèle
admin.site.register(AllAdmin, AllAdminAdmin)