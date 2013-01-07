from django.db import models
from django.conf import settings

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