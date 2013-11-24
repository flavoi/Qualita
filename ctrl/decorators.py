"""
    Associabili a viste in tutte le app del progetto.
    Controllano alcuni importanti funzionalita` come le votazioni.
"""

from functools import wraps
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.decorators import available_attrs

