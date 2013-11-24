# Django models for app ctrl

from django.db import models
import datetime

TODAY = datetime.date.today()

"""
    Block all functionalities if stato is False.
    The decorator will calculate the current period reading the datefields.
"""
class Stagione(models.Model):
    STATI = (
        ('0', 'chiusa'),
        ('1', 'aperta'),
    )
    data_inizio = models.DateField(default=TODAY)
    data_fine = models.DateField(default=TODAY) # Should always be greater than data_inizio
    stato = models.CharField(max_length=6, choices=STATI)
    
    class Meta:
        verbose_name_plural = "Stagioni"
    
    def __unicode__(self):
        return u'%s' % (self.id)