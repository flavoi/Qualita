# Django assets
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.utils.functional import curry
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Gestione messaggi
from django.contrib import messages

# App assets
from models import *
from forms import ValutazioniForm

# Renderizza la pagina iniziale
@login_required
def get_interrogazioni(request):
    interrogazioni = Interrogazione.objects.all()
    context = {
        'interrogazioni':interrogazioni,
    }
    return render_to_response('interrogazioni.html', RequestContext(request, context))

# Gestione valutazioni
"""
    @param id_interrogazione: id Interrogazione corrente
    @param current_url:       id URL corrente
"""
@login_required
def get_valutazioni(request, id_interrogazione, current_url=None):

    ValutazioniFormSet = modelformset_factory(Score, form=ValutazioniForm, extra=1, max_num=1)
    
    # Raccolta dati e Paginazione
    page = request.GET.get('pagina')
    
    interrogazione = Interrogazione.objects.get(id=id_interrogazione)                
    url_list = interrogazione.url.all()
    paginator = Paginator(url_list, 1)
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
        formset = ValutazioniFormSet(request.POST, request.FILES) 
        if formset.is_valid():
            for form in formset:
                form = form.save(commit=False)
                form.url = url
                form.author = request.user
        formset.save()
        if formset.has_changed():
            messages.success(request, "Voto n. %s inviato con successo!" % url.id )
        return HttpResponseRedirect(reverse("valutazioni", args=(id_interrogazione,)) + "?pagina=" + page)
    else:
        page_query = Score.objects.filter(url__in = [url.id for url in url_list]).filter(author=request.user)
        interrogazione = Interrogazione.objects.get(id=id_interrogazione)
        formset = ValutazioniFormSet(queryset=page_query)
        context = {
            'url_list': url_list,
            'formset': formset,
            'id_interrogazione': id_interrogazione,
            'interrogazione': interrogazione,
        }
        return render_to_response('valutazioni.html', RequestContext(request, context))