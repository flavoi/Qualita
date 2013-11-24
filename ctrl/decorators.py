"""
    Associabili a viste in tutte le app del progetto.
    Controllano alcuni importanti funzionalita` come le votazioni.
"""

# App assets
from models import *

# Django assets
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils.decorators import available_attrs
from functools import wraps

# Utils
import datetime

# Inibisce voti in caso di periodo chiuso
def open_period_only(view_func):
    @wraps(view_func, assigned=available_attrs(view_func))
    def wrapper(request, *args, **kwargs):
        today = datetime.date.today()
        stagione = Stagione.objects.filter(data_inizio__lte=today).filter(data_fine__gte=today).filter(stato='1').count() # Assunzione: una sola stagione aperta per periodo
        if stagione:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse("parcheggio"))
    return wrapper