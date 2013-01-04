from django.conf.urls import patterns, include, url
from django.conf import settings

# Attivazione Admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
)

urlpatterns += patterns('core',
    url(r'^$', 'views.render_to_home', name="home"),
)

if settings.DEBUG == True:
    # Supporto a MEDIA_ROOT e JQUERY_ROOT (solo in sviluppo)
    urlpatterns += patterns('',
        url(r'^uploaded/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT,}),
        url(r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT + 'js/',}),
    )
