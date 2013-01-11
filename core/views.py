# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
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
def valutazioni(request, id_valutazione):
    if request.method == 'POST': 
        url = get_object_or_404(URL, id=id_valutazione)
        form = ValutazioniForm(request.POST)
        if form.is_valid(): 
            form = form.save(commit=False)
            form.url = url
            form.author = request.user
            form.save() 
            return HttpResponse("<h1 style='text-align:center;'> Grazie per aver votato </h1>")
    else:
        form = ValutazioniForm(
            initial = {
            "rilevanza": "0",
            "leggibilita": "0",
            "fonte": "0",
            "stile": "0",
            })
        interrogazione = Interrogazione.objects.get(id=id_valutazione)
        url_list = interrogazione.url.all()
        
        # Supporto per paginazione
        paginator = Paginator(url_list, 1)
        page = request.GET.get('page')
        try:
            url = paginator.page(page)
        except PageNotAnInteger:
            # Prima pagina
            url = paginator.page(1)
        except EmptyPage:
            # Pagina out-of-range
            url = paginator.page(paginator.num_pages)
            
    context = {
        'url':url,
        'form':form,
        'id_valutazione':id_valutazione,
    }
    return render_to_response('valutazioni.html', RequestContext(request, context))