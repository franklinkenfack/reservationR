from django.contrib import admin
from .models import Agency

class AgencyAdmin(admin.ModelAdmin):
    list_display = ('agency_id', 'agency_name', 'localite', 'city', 'country', 'state')

admin.site.register(Agency, AgencyAdmin)