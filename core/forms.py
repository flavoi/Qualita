# -*- coding: utf-8 -*-

from models import Score, get_valutazioni
from django.forms import ModelForm
from django.forms.fields import ChoiceField
from django.forms.widgets import RadioSelect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, HTML
from crispy_forms.bootstrap import InlineRadios, StrictButton, FormActions
from django.utils.safestring import mark_safe

VALUTAZIONI_SCELTE = get_valutazioni()

def aiuto(title, label):
    head = mark_safe("<strong>%s&nbsp;</strong>" % title)
    tail = mark_safe("<a href='#' class='pophelp' data-trigger='hover' rel='popover' data-original-title='%s' data-content='%s'> <i class='icon-info-sign'></i> </a>" % (title, label))
    return head + tail

class ValutazioniForm(ModelForm):

    AIUTO_RILEVANZA = "Aiuto rilevanza!"
    rilevanza = ChoiceField(
        required = True,
        widget = RadioSelect, 
        choices = VALUTAZIONI_SCELTE, 
        label = aiuto("Rilevanza", AIUTO_RILEVANZA),
        initial = "1",
    )
    
    leggibilita = ChoiceField(
        required=  True,
        widget = RadioSelect, 
        choices = VALUTAZIONI_SCELTE, 
        label = aiuto("Leggibilità", "aiuto leggibilità!"),
        initial = "1",
    )

    fonte = ChoiceField(
        required = True,
        widget = RadioSelect, 
        choices = VALUTAZIONI_SCELTE,
        label = aiuto("Fonte", "aiuto fonte!"),
        initial = "1",
    )
    
    stile = ChoiceField(
        required = True,
        widget = RadioSelect,
        choices = VALUTAZIONI_SCELTE, 
        label = aiuto("Stile", "aiuto stile!"),
        initial = "1",
    )

    class Meta:
        model = Score
        exclude = ('id', 'url', 'author', 'commento')



    def __init__(self, *args, **kwargs):
        super(ValutazioniForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            InlineRadios(
                'rilevanza',
                'leggibilita',
                'fonte',
                'stile',
                ),
            FormActions(
                Submit('conferma-voto', 'Conferma', css_class='btn-warning')
            )
        )