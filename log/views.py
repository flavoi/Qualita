# Create your views here.
from models import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

# Interrogazione e impaginazione Storico delle Versioni
@login_required
def notes(request):
    pagename = "Note di Rilascio"
    legend = "Storico delle Versioni"
    releases = Release.objects.all().order_by('data_rilascio').reverse()
    contex = {
        'pagename':pagename,
        'legend':legend,
        'releases':releases,
    }
    return render_to_response('releases.html', RequestContext(request, contex))

# Visualizzazione in dettaglio delle Note di Rilascio per singola versione
@login_required
def notes_detail(request, id_release):
    release = Release.objects.get(pk=id_release)
    notes = Nota.objects.filter(release = release)
    pagename = "Note di Rilascio"
    legend = pagename + " (Release v" + release.versione + ")"
    contex = {
        'pagename':pagename,
        'legend':legend,
        'notes':notes,
    }
    return render_to_response('notes.html', RequestContext(request, contex))

# Visualizzazione in dettaglio delle versioni in via di sviluppo
@login_required
def notes_upcoming(request):
    notes = Nota.objects.filter(ultimata=0)
    nonews = 0
    if notes.count() == 0:
        notes = None
        nonews = 1
    pagename = "In Sviluppo"
    legend = pagename
    contex = {
        'pagename':pagename,
        'notes':notes,
        'legend':legend,
        'nonews':nonews,
    }
    return render_to_response('notes.html', RequestContext(request, contex))
