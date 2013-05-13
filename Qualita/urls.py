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
    url(r'^$', 'views.render_to_home', name="home"),
    url(r'^valutazioni/interrogazione(?P<id_interrogazione>\d{1,10})/$', 'views.valutazioni', name="valutazioni"),
    url(r'^valutazioni/interrogazione(?P<id_interrogazione>\d{1,10})/url(?P<current_url>\d{1,10})$', 'views.valutazioni', name="votazioni"),
)

# App auth
urlpatterns += patterns('auth',
    url(r'^registrazione/$', 'views.registrazione', name="registrazione"),
)

if settings.DEBUG == True:
    # Supporto a MEDIA_ROOT e JQUERY_ROOT (solo in sviluppo)
    urlpatterns += patterns('',
        url(r'^uploaded/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
        url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT + 'js/',}),
    )