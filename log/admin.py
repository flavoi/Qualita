# Pannello admin: app log

from django.contrib import admin
from log.models import *

class NotaInline(admin.TabularInline):
    model = Nota
    extra = 3

class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('data_rilascio','versione')
    inlines = [NotaInline]

admin.site.register(Release, ReleaseAdmin)