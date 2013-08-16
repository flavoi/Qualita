from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class URL(models.Model):
    indirizzo = models.URLField()
    percorso_su_disco = models.FileField(upload_to=settings.MEDIA_ROOT, blank=True)
    
    class Meta:
        verbose_name_plural = "URL"
    
    def __unicode__(self):
        return u'%s' % (self.indirizzo)
    
    def get_percorso(self):
        return self.percorso_su_disco.path[len(settings.MEDIA_ROOT):]

class Interrogazione(models.Model):
    titolo = models.CharField(max_length=50)
    descrizione = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)
    url = models.ManyToManyField(URL)
    
    class Meta:
        verbose_name_plural = "Interrogazioni"
    
    def __unicode__(self):
        return u'%s' % (self.titolo)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titolo)
        super(Interrogazione, self).save(*args, **kwargs)

VALUTAZIONI_SCELTE = (
        ('1', '1'), 
        ('2', '2'), 
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
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

