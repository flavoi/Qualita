from django.forms import ModelForm
from django.forms.fields import ChoiceField
from django.forms.widgets import RadioSelect
from models import *

VALUTAZIONI_SCELTE = (
    (0, 'scarso'), 
    (1, 'insufficiente'), 
    (2, 'sufficiente'),
    (3, 'buono'),
)

"""
class ValutazioniForm(forms.Form):
    rilevanza = forms.ChoiceField(required=True,
        widget=RadioSelect, choices=VALUTAZIONI_SCELTE)
    leggibilita = forms.ChoiceField(required=True,
        widget=RadioSelect, choices=VALUTAZIONI_SCELTE)
    fonte = forms.ChoiceField(required=True,
        widget=RadioSelect, choices=VALUTAZIONI_SCELTE)
    stile = forms.ChoiceField(required=True,
        widget=RadioSelect, choices=VALUTAZIONI_SCELTE)
    commento = forms.CharField(widget=forms.Textarea)
"""
class ValutazioniForm(ModelForm):
    rilevanza = ChoiceField(required=True,
        widget=RadioSelect, choices=VALUTAZIONI_SCELTE)
    leggibilita = ChoiceField(required=True,
        widget=RadioSelect, choices=VALUTAZIONI_SCELTE)
    fonte = ChoiceField(required=True,
        widget=RadioSelect, choices=VALUTAZIONI_SCELTE)
    stile = ChoiceField(required=True,
        widget=RadioSelect, choices=VALUTAZIONI_SCELTE)
    class Meta:
        model = Score
        exclude = ('url',)