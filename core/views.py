# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from models import *
from forms import ValutazioniForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Renderizza la pagina iniziale
@login_required
def render_to_home(request):
    interrogazioni = Interrogazione.objects.all()
    context = {
        'interrogazioni':interrogazioni,
    }
    return render_to_response('home.html', RequestContext(request, context))

# Gestione valutazioni
"""
    @param id_valutazione: in caso di richiesta POST corrisponde a url.id,
                           altrimenti a interrogazione.id.
"""
@login_required
def valutazioni(request, id_interrogazione, current_url=None):
    messaggio = None
    interrogazione = Interrogazione.objects.get(id=id_interrogazione)                # Raccolta dati e paginazione
    url_list = interrogazione.url.all()
    paginator = Paginator(url_list, 1)
    page = request.GET.get('page')
    try:
        url_list = paginator.page(page)
    except PageNotAnInteger:
        # Prima pagina
        url_list = paginator.page(1)
    except EmptyPage:
        # Pagina out-of-range
        url_list = paginator.page(paginator.num_pages) 

    if request.method == 'POST': 
        url = get_object_or_404(URL, id=current_url)
        form = ValutazioniForm(request.POST)
        if form.is_valid(): 
            valutazione = form.save(commit=False)
            valutazione.url = url
            valutazione.author = request.user
            valutazione.save() 
            messaggio = "Valutazione salvata con successo."
    else:
        form = ValutazioniForm(
            initial = {
            "rilevanza": "0",
            "leggibilita": "0",
            "fonte": "0",
            "stile": "0",
            })       

    context = {
        'url_list': url_list,
        'form': form,
        'id_interrogazione': id_interrogazione,
        'messaggio': messaggio,
    }
    return render_to_response('valutazioni.html', RequestContext(request, context))