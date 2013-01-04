# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

# Renderizza la pagina iniziale
def render_to_home(request):
    contex = {}
    return render_to_response('base.html', RequestContext(request, contex))
