from django.contrib import admin
from .models import ServiceAvailable

class ServiceAvailableAdmin(admin.ModelAdmin):
    list_display = ('id', 'wifi', 'electric_socket', 'air_conditioning', 'toilet', 'seatbelt', 'entertainment_screen')

admin.site.register(ServiceAvailable, ServiceAvailableAdmin)