from django.conf.urls import patterns, include, url
from django.conf import settings

# Attivazione Admin
from django.contrib import admin
admin.autodiscover()

# Generale
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^grappelli/', include('grappelli.urls')),
)

# App core
urlpatterns += patterns('core',
    url(r'^$', 'views.render_to_home', name="home"),
    url(r'^valutazioni/interrogazione(?P<id_interrogazione>\d{1,10})/$', 'views.valutazioni', name="valutazioni"),
    url(r'^valutazioni/interrogazione(?P<id_interrogazione>\d{1,10})/url(?P<current_url>\d{1,10})$', 'views.valutazioni', name="votazioni"),
)

# App auth
urlpatterns += patterns('auth',
    url(r'login/$', 'views.login', {'template_name':'login.html'}, name="login"),
    url(r'logout/$', 'views.logout_then_login', {'login_url':'login'}, name="logout"),
)

if settings.DEBUG == True:
    # Supporto a MEDIA_ROOT e JQUERY_ROOT (solo in sviluppo)
    urlpatterns += patterns('',
        url(r'^uploaded/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
        url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT + 'js/',}),
    )
