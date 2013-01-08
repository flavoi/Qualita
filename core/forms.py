from django.forms.fields import DateField, ChoiceField, MultipleChoiceField
from django.forms.widgets import RadioSelect, Textarea
from django import forms

VALUTAZIONI_SCELTE = (
    (0, 'scarso'), 
    (1, 'insufficiente'), 
    (2, 'sufficiente'),
    (3, 'buono'),
)

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