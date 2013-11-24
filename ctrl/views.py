# Django assets
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from ctrl.models import *

@login_required
def park_here(request):
    context = {
        'ultima_stagione': Stagione.objects.latest('data_fine')
    }
    return render_to_response("fine_stagione.html", RequestContext(request, context))