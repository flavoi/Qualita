from django.db import models
import datetime

TODAY = datetime.date.today()

"""
    Aperta blocca l'operativita` se posta a False.
    Il decoratore dedurra` la stagione corrente dalla data inizio e dalla durata.
    Da prevedere vincolo su Stagione non promiscue.
"""
# Pannello di controllo votazioni
class Stagione(models.Model):
    STATI = (
        ('0', 'chiusa'),
        ('1', 'aperta'),
    )
    data_inizio = models.DateField(default=TODAY)
    data_fine = models.DateField(default=TODAY) # Da vincolare maggiore stretta alla prima
    stato = models.CharField(max_length=6, choices=STATI)
    
    class Meta:
        verbose_name_plural = "Stagioni"
    
    def __unicode__(self):
        return u'%s' % (self.id)