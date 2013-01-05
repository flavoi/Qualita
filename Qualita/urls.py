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
)

# App auth
urlpatterns += patterns('auth',
    url(r'login/$', 'views.login', {'template_name':'login.html'}, name="login"),
    url(r'logout/$', 'views.logout_then_login', {'login_url':'login'}, name="logout"),
)

# App log
urlpatterns += patterns('log',
    url(r'^note/$', 'views.notes', name="notes"),
    url(r'^note/(?P<id_release>\d{1,10})/$', 'views.notes_detail', name="notes_detail"),
    url(r'^note/sviluppo/$', 'views.notes_upcoming', name="notes_upcoming"),
)

if settings.DEBUG == True:
    # Supporto a MEDIA_ROOT e JQUERY_ROOT (solo in sviluppo)
    urlpatterns += patterns('',
        url(r'^uploaded/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
        url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT + 'js/',}),
    )
