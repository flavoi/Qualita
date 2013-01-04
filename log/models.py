# Modelli per la gestione dello storico delle versioni
from django.db import models
import os, datetime

# Raccoglitore di note per data e versione
class Release(models.Model):
    data_rilascio = models.DateField(verbose_name="Data di Rilascio", default=datetime.date.today())
    versione = models.CharField(max_length=10)
    class Meta:
        verbose_name_plural = 'Release'
    def __unicode__(self):
        return u'v%s - %s' % (self.versione, self.data_rilascio.strftime('%d/%m/%Y'))

# Dettaglio nota
class Nota(models.Model):
    titolo = models.CharField(max_length=40)
    descrizione = models.TextField()
    ultimata = models.IntegerField(choices=((1, "si"),(0, "no")), default=0)
    release = models.ForeignKey(Release)
    class Meta:
        verbose_name_plural = "Note"
    def __unicode__(self):
        return u'%s' % self.titolo
