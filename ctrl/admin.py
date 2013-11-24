from django.contrib import admin
from models import *

class StagioneAdmin(admin.ModelAdmin):
    list_display = ('data_inizio', 'durata', 'stato')
admin.site.register(Stagione, StagioneAdmin)