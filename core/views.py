# Django assets
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.forms.models import modelformset_factory
from django.utils.functional import curry
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# App assets
from models import *
from forms import ValutazioniForm

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
    @param id_interrogazione: id Interrogazione corrente
    @param current_url:       id URL corrente
"""
@login_required
def valutazioni(request, id_interrogazione, current_url=None):
    ValutazioniFormSet = modelformset_factory(Score, form=ValutazioniForm, extra=1, max_num=1)
    
    # Raccolta dati e Paginazione
    page = request.GET.get('page')
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
        ids = []
        if formset.is_valid():
            for form in formset:
                form = form.save(commit=False)
                form.url = url
                form.author = request.user
                ids.append(form.id)
        formset.save()
        if formset.has_changed():
            request.session['msg_ok'] = "Voto n. %s inviato con successo!" % ids 
        return HttpResponseRedirect(reverse("valutazioni", args=(id_interrogazione,)) + "?page=" + page)
    else:
        page_query = Score.objects.filter(id__in = [url.id for url in url_list])
        formset = ValutazioniFormSet(queryset=page_query)
        context = {
            'url_list': url_list,
            'formset': formset,
            'id_interrogazione': id_interrogazione,
        }
        # Pulizia sessione
        if request.session.get('msg_ok'):
            context['msg_ok'] = request.session.get('msg_ok')
            del request.session['msg_ok']
        return render_to_response('valutazioni.html', RequestContext(request, context))