from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class URL(models.Model):
    indirizzo = models.URLField()
    percorso_su_disco = models.FilePathField(path=settings.MEDIA_ROOT)
    class Meta:
        verbose_name_plural = "URL"
    def __unicode__(self):
        return u'%s' % (self.indirizzo)

class Interrogazione(models.Model):
    titolo = models.CharField(max_length=50)
    descrizione = models.TextField(max_length=50)
    url = models.ManyToManyField(URL)
    class Meta:
        verbose_name_plural = "Interrogazioni"
    def __unicode__(self):
        return u'%s' % (self.titolo)

VALUTAZIONI_SCELTE = (
        ('0', 'non classificabile'), 
        ('1', 'scarso'), 
        ('2', 'insufficiente'), 
        ('3', 'sufficiente'),
        ('4', 'buono'),
    )
def get_valutazioni():
    return VALUTAZIONI_SCELTE

class Score(models.Model):
    rilevanza = models.CharField(max_length=2, choices=VALUTAZIONI_SCELTE)
    fonte = models.CharField(max_length=2, choices=VALUTAZIONI_SCELTE)
    leggibilita = models.CharField(max_length=2, choices=VALUTAZIONI_SCELTE)
    stile = models.CharField(max_length=2, choices=VALUTAZIONI_SCELTE)
    commento = models.TextField(blank=True)
    url = models.ForeignKey(URL, null=True, blank=True)
    author = models.ForeignKey(User)
    def __unicode__(self):
        return u'Rilevanza: %s' % (self.rilevanza)