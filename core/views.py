# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from models import *
from forms import ValutazioniForm

# Renderizza la pagina iniziale
@login_required
def render_to_home(request):
    interrogazioni = Interrogazione.objects.all()
    contex = {
        'interrogazioni':interrogazioni,
    }
    return render_to_response('home.html', RequestContext(request, contex))

# Gestione valutazioni
@login_required
def valutazioni(request, id_interrogazione):
    interrogazione = Interrogazione.objects.get(id=id_interrogazione)
    url = interrogazione.url.all()
    form = ValutazioniForm()
    contex = {
        'url':url,
        'form':form,
    }
    return render_to_response('valutazioni.html', RequestContext(request, contex))