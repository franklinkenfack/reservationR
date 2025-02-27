from django.contrib import admin
from .models import Line

class LineAdmin(admin.ModelAdmin):
    list_display = ('line_id', 'starting_point', 'arrival_location','state')

admin.site.register(Line, LineAdmin)