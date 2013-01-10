from django.forms import ModelForm
from django.forms.fields import ChoiceField
from django.forms.widgets import RadioSelect
from models import *

VALUTAZIONI_SCELTE = get_valutazioni()

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
        exclude = ('url', 'author', 'commento')