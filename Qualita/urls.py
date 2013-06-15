from django.conf.urls import patterns, include, url
from django.conf import settings
from emailusernames.forms import EmailAuthenticationForm

# Attivazione Admin
from django.contrib import admin
admin.autodiscover()

# Generale
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'login.html', 'authentication_form': EmailAuthenticationForm}, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}, name="logout"),
)

# App core
urlpatterns += patterns('core',
    url(r'^$', 'views.get_interrogazioni', name="home"),
    url(r'^valutazioni/interrogazione(?P<id_interrogazione>\d{1,10})/$', 'views.get_valutazioni', name="valutazioni"),
    url(r'^valutazioni/interrogazione(?P<id_interrogazione>\d{1,10})/url(?P<current_url>\d{1,10})$', 'views.get_valutazioni', name="votazioni"),
)

# App auth
urlpatterns += patterns('auth',
    url(r'^registrazione/$', 'views.registrazione', name="registrazione"),
)