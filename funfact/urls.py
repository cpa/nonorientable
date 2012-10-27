from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# STATICFILES_DIRS = ("/Users/cpa/prog/funfact/")
STATIC_URL = 'static/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'funfact.views.home', name='home'),
    # url(r'^funfact/', include('funfact.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'funlog.views.index', name='index'),
    url(r'^a-propos/$', 'funlog.views.apropos', name='apropos'),
    url(r'^mentions-legales/$', 'funlog.views.legal', name='legal'),
    url(r'^funfacts/all/$', 'funlog.views.funfactsall', name='all'),
    url(r'^funfacts/$', 'funlog.views.funfactsall', name='all'),
    url(r'^funfacts/(\S+)$', 'funlog.views.detail', name='detail')
)

# ... the rest of your URLconf goes here ...

urlpatterns += staticfiles_urlpatterns()
