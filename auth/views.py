# Django assets
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext

# Avoid shadowing the login() and logout() views below.
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout, authenticate

# Email as username
from forms import RegistrationForm as EmailUserCreationForm
from emailusernames.utils import create_user, get_user, user_exists

# Gestione messaggi
from django.contrib import messages

def registrazione(request):
    form_error = None
    if request.method == "POST":
        user_form = EmailUserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            email = request.POST['email']
            password = request.POST['password1']
            new_user = authenticate(email=email, password=password)
            auth_login(request, new_user)
            messages.info(request, "Registrazione avvenuta con successo.")
            return HttpResponseRedirect(reverse("home"))
        else:
            form_error = True
    user_form = EmailUserCreationForm()
    context = {
        'form': user_form,
        'form_error': form_error,
    }
    return render_to_response('registrazione.html', RequestContext(request, context))