# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

# Renderizza la pagina iniziale
@login_required
def render_to_home(request):
    contex = {}
    return render_to_response('home.html', RequestContext(request, contex))
