# -*- coding: utf-8 -*-

from models import Score, get_valutazioni
from django.forms import ModelForm
from django.forms.fields import ChoiceField
from django.forms.widgets import RadioSelect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML
from crispy_forms.bootstrap import InlineRadios, StrictButton, FormActions

VALUTAZIONI_SCELTE = get_valutazioni()

class ValutazioniForm(ModelForm):

    rilevanza = ChoiceField(
        required=True,
        widget=RadioSelect, 
        choices=VALUTAZIONI_SCELTE, 
        initial="1",
    )

    leggibilita = ChoiceField(
        required=True,
        widget=RadioSelect, 
        choices=VALUTAZIONI_SCELTE, 
        label="Leggibilità", 
        initial="1",
    )

    fonte = ChoiceField(
        required=True,
        widget=RadioSelect, 
        choices=VALUTAZIONI_SCELTE,
        initial="1",
    )
    
    stile = ChoiceField(
        required=True,
        widget=RadioSelect,
        choices=VALUTAZIONI_SCELTE, 
        initial="1",
    )

    class Meta:
        model = Score
        exclude = ('id', 'url', 'author', 'commento')

    def __init__(self, *args, **kwargs):
        super(ValutazioniForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            InlineRadios(
                'rilevanza',
                HTML("""
                    <a href="#" id="example" class="btn btn-success" data-trigger="hover" rel="popover" data-content="It's so simple to create a tooltop for my website!" data-original-title="Twitter Bootstrap Popover">hover for popover</a>
                """),
                'leggibilita',
                'fonte',
                'stile',
                ),
            FormActions(
                Submit('conferma-voto', 'Conferma', css_class='btn-warning')
            )
        )