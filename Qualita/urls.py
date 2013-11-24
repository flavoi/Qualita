from django.conf.urls import patterns, include, url
from django.conf import settings
from emailusernames.forms import EmailAuthenticationForm

# Attivazione Admin
from django.contrib import admin
admin.autodiscover()

# Generale
urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^admin/',  include(admin.site.urls)), # admin site
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'login.html', 'authentication_form': EmailAuthenticationForm}, name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}, name="logout"),
)

# App core
urlpatterns += patterns('core',
    url(r'^$', 'views.get_interrogazioni', name="home"),
    url(r'^valutazioni/interrogazione/(?P<id_interrogazione>\d{1,10})/$', 'views.get_valutazioni', name="valutazioni_old"),
    url(r'^valutazioni/interrogazione/(?P<id_interrogazione>\d{1,10})/(?P<slug>[\w-]+)/$', 'views.get_valutazioni', name="valutazioni"),
    url(r'^valutazioni/interrogazione/(?P<id_interrogazione>\d{1,10})/(?P<slug>[\w-]+)/url(?P<current_url>\d{1,10})/$', 'views.get_valutazioni', name="votazioni"),
)

# App auth
urlpatterns += patterns('auth',
    url(r'^registrazione/$', 'views.registrazione', name="registrazione"),
)

# App captcha
urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)

# App ctrl
urlpatterns += patterns('ctrl',
    url(r'^stagione/chiusa', 'views.park_here', name="parcheggio"),
)