# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django.forms.fields import ChoiceField
from django.forms.widgets import RadioSelect
from models import *

VALUTAZIONI_SCELTE = get_valutazioni()

class ValutazioniForm(ModelForm):
    rilevanza = ChoiceField(required=True,
        widget=RadioSelect, choices=VALUTAZIONI_SCELTE, initial="0")
    leggibilita = ChoiceField(required=True,
        widget=RadioSelect, choices=VALUTAZIONI_SCELTE, label="Leggibilità", initial="0")
    fonte = ChoiceField(required=True,
        widget=RadioSelect, choices=VALUTAZIONI_SCELTE, initial="0")
    stile = ChoiceField(required=True,
        widget=RadioSelect, choices=VALUTAZIONI_SCELTE, initial="0")
    class Meta:
        model = Score
        exclude = ('id', 'url', 'author', 'commento')