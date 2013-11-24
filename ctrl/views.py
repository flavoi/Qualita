# Django assets
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext

@login_required
def park_here(request):
    context = {}
    return render_to_response("closed_period.html", RequestContext(request, context))