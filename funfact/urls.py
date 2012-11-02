from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

STATICFILES_DIRS = ("/var/www/nonorientable.fr/funlog/static/")
STATIC_URL = 'static/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'funfact.views.home', name='home'),
    # url(r'^funfact/', include('funfact.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^a-propos/$', 'funfact.views.apropos', name='apropos'),
    url(r'^mentions-legales/$', 'funfact.views.legal', name='legal'),
    url(r'^funfacts/all/$', 'funfact.views.funfactsall', name='all'),
    url(r'^funfacts/$', 'funfact.views.funfactsall', name='all'),
    url(r'^funfacts/(\S+)$', 'funfact.views.detail', name='detail'),
    url(r'^$', 'funfact.views.index', name='index'),
)

# ... the rest of your URLconf goes here ...

urlpatterns += staticfiles_urlpatterns()
