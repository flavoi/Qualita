from django.contrib import admin
from models import *

class InterrogazioneAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'descrizione')

class URLAdmin(admin.ModelAdmin):
    list_display = ('indirizzo', 'percorso_su_disco')


admin.site.register(Interrogazione, InterrogazioneAdmin)
admin.site.register(URL, URLAdmin)